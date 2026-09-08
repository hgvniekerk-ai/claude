#!/usr/bin/env python3
"""
YouTube -> Meditative Audio Pipeline

Transform YouTube channels into long-form, flowing audio you can absorb
while walking or on the treadmill.

Usage:
    python bxtchesaintshit_audio.py <channel_or_playlist_url> [options]

Options:
    --videos N         Number of videos to process (default: 8)
    --voice VOICE      Voice key: ryan, william, guy, natasha, sonia, aria (default: ryan)
    --length MINS      Target listen length in minutes: 20, 40, 60, 80 (default: 40)
    --tone TONE        contemplative / philosophical / energetic (default: contemplative)
    --after DATE       Only videos after YYYYMMDD
    --output DIR       Output directory (default: ~/audio_episodes)
    --script-only      Generate script text file, no audio
"""

import argparse
import asyncio
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import anthropic
import edge_tts
from youtube_transcript_api import YouTubeTranscriptApi


# ─── Voice Configuration ───────────────────────────────────────────────────────

VOICES = {
    "ryan":    "en-GB-RyanNeural",
    "william": "en-AU-WilliamNeural",
    "guy":     "en-US-GuyNeural",
    "natasha": "en-AU-NatashaNeural",
    "sonia":   "en-GB-SoniaNeural",
    "aria":    "en-US-AriaNeural",
}

LENGTH_TO_WORDS = {20: 2500, 40: 5000, 60: 7500, 80: 10000}

SYSTEM_PROMPT = (
    "You are a contemplative writer who distills ideas from talks, lectures, "
    "and conversations into long, flowing meditative narratives. Your writing "
    "is unhurried, layered, and rich with meaning. It sounds beautiful when "
    "read aloud.\n\n"
    "You do NOT summarize. You TRANSMIT ideas — as if the listener is walking "
    "through a landscape of thought.\n"
    "You write in flowing prose with no bullet points, no headers, no lists.\n"
    "You weave ideas from multiple sources into a single unified voice.\n"
    "You speak directly to the listener using \"you\" — drawing them into the ideas.\n"
    "You allow ideas to breathe — some thoughts are stated simply, then allowed "
    "to linger.\n"
    "You use rhythm, repetition, and contrast deliberately.\n"
    "You avoid jargon and academic stiffness. Keep it grounded and human.\n"
    "Your tone is warm, spacious, and slightly philosophical."
)


# ─── Step 1: Fetch Video List ──────────────────────────────────────────────────

def fetch_channel_videos(url, max_videos=10, after_date=None):
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--dump-json",
        "--playlist-end", str(max_videos),
        "--no-warnings",
    ]
    if after_date:
        cmd += ["--dateafter", after_date]
    cmd.append(url)

    result = subprocess.run(cmd, capture_output=True, text=True)

    videos = []
    for line in result.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            v = json.loads(line)
            videos.append({
                "id": v.get("id"),
                "title": v.get("title"),
                "url": v.get("url") or f"https://youtube.com/watch?v={v.get('id')}",
                "duration": v.get("duration"),
                "upload_date": v.get("upload_date"),
            })
        except json.JSONDecodeError:
            continue
    return videos


# ─── Step 2: Download Transcripts ──────────────────────────────────────────────

def get_transcript(video_id, preferred_langs=None):
    if preferred_langs is None:
        preferred_langs = ["en"]
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        try:
            transcript = transcript_list.find_transcript(preferred_langs)
        except Exception:
            transcript = transcript_list.find_generated_transcript(preferred_langs)

        entries = transcript.fetch()
        text = " ".join(e["text"].replace("\n", " ") for e in entries)
        return text.strip()
    except Exception as e:
        print(f"  Warning: Could not fetch transcript for {video_id}: {e}")
        return None


def fetch_all_transcripts(videos):
    enriched = []
    for v in videos:
        print(f"  Fetching transcript: {v['title'][:60]}...")
        transcript = get_transcript(v["id"])
        if transcript:
            v["transcript"] = transcript
            v["transcript_words"] = len(transcript.split())
            enriched.append(v)
        else:
            print(f"  [skip] No transcript available: {v['title'][:60]}")
    print(f"\n  {len(enriched)}/{len(videos)} transcripts retrieved.")
    return enriched


# ─── Step 3: Synthesize Meditative Script ──────────────────────────────────────

def build_synthesis_prompt(videos, target_words, tone="contemplative"):
    sources_text = ""
    for i, v in enumerate(videos, 1):
        sources_text += f"\n\n--- SOURCE {i}: {v['title']} ---\n{v['transcript'][:8000]}"

    tone_note = ""
    if tone == "energetic":
        tone_note = "Use a slightly more energetic, motivating tone — still contemplative but with momentum."
    elif tone == "philosophical":
        tone_note = "Lean into philosophical depth. Quote ideas indirectly. Allow paradox and uncertainty."

    return (
        f"Below are transcripts from {len(videos)} videos.\n\n"
        f"Your task: synthesize the most powerful, resonant, and universal ideas from ALL of them into a single "
        f"continuous meditative narrative of approximately {target_words} words.\n\n"
        f"{tone_note}\n\n"
        "Instructions:\n"
        "- Find the through-line — what is the deeper theme connecting these talks?\n"
        "- Extract the 5-10 most potent ideas across all sources\n"
        "- Weave them into ONE unified flowing narrative — not video-by-video\n"
        "- Speak directly to a listener walking or in quiet movement\n"
        "- Write as if the ideas are gently landing, not being delivered\n"
        "- Begin without preamble — drop the listener straight into the first idea\n"
        "- End with a sense of open reflection, not conclusion\n"
        "- Do NOT mention video titles, channel names, or speaker names\n"
        "- Do NOT use headers, bullets, or section breaks\n"
        f"- Target length: {target_words} words\n"
        f"{sources_text}\n\n"
        "Begin the narrative now:"
    )


def synthesize_script(videos, target_words=5000, tone="contemplative"):
    client = anthropic.Anthropic()
    prompt = build_synthesis_prompt(videos, target_words, tone)

    print(f"  Synthesizing {len(videos)} transcripts into ~{target_words} word narrative...")

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8192,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )

    script = message.content[0].text
    actual_words = len(script.split())
    print(f"  Script generated: {actual_words} words (~{actual_words // 125} min listen time)")
    return script


# ─── Step 4: Generate Audio (TTS) ─────────────────────────────────────────────

async def text_to_audio(script, output_path, voice_key="ryan", rate="-10%", pitch="-5Hz"):
    voice = VOICES.get(voice_key, VOICES["ryan"])
    communicate = edge_tts.Communicate(
        text=script,
        voice=voice,
        rate=rate,
        pitch=pitch,
    )
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    await communicate.save(output_path)
    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"  Audio saved: {output_path} ({size_mb:.1f} MB)")


def generate_audio(script, output_path, voice_key="ryan", pace="meditative"):
    rate_map = {
        "meditative": "-15%",
        "normal": "-5%",
        "energetic": "+5%",
    }
    rate = rate_map.get(pace, "-15%")
    asyncio.run(text_to_audio(script, output_path, voice_key=voice_key, rate=rate))


# ─── Pipeline Orchestrator ─────────────────────────────────────────────────────

def slugify(text):
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_-]+", "_", text).strip("_")[:50]


def run_pipeline(args):
    print(f"\n  YouTube -> Meditative Audio Pipeline")
    print(f"  Source:  {args.url}")
    print(f"  Videos:  {args.videos}")
    print(f"  Voice:   {args.voice}")
    print(f"  Length:  ~{args.length} min")
    print(f"  Tone:    {args.tone}\n")

    # 1. Fetch video list
    print("-" * 50)
    print("Step 1/4 -- Fetching video list...")
    videos = fetch_channel_videos(args.url, max_videos=args.videos, after_date=args.after)
    if not videos:
        print("No videos found. Check the URL and try again.")
        sys.exit(1)
    print(f"  Found {len(videos)} videos.\n")

    # 2. Get transcripts
    print("Step 2/4 -- Downloading transcripts...")
    videos_with_transcripts = fetch_all_transcripts(videos)
    if len(videos_with_transcripts) < 3:
        print("Too few transcripts available. Need at least 3 for a meaningful episode.")
        sys.exit(1)
    print()

    # 3. Synthesize script
    print("Step 3/4 -- Synthesizing meditative script...")
    target_words = LENGTH_TO_WORDS.get(args.length, 5000)
    script = synthesize_script(videos_with_transcripts, target_words=target_words, tone=args.tone)
    print()

    # Save script and metadata
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    channel_slug = slugify(args.url.rstrip("/").split("/")[-1] or "episode")
    output_dir = Path(args.output).expanduser() / channel_slug
    output_dir.mkdir(parents=True, exist_ok=True)

    script_path = output_dir / f"{timestamp}_script.txt"
    script_path.write_text(script)
    print(f"  Script saved: {script_path}")

    meta = {
        "generated": timestamp,
        "source_url": args.url,
        "videos": [{"title": v["title"], "id": v["id"]} for v in videos_with_transcripts],
        "word_count": len(script.split()),
        "voice": args.voice,
        "tone": args.tone,
    }
    (output_dir / f"{timestamp}_meta.json").write_text(json.dumps(meta, indent=2))

    if args.script_only:
        print("\n  Script-only mode. Done.")
        return

    # 4. Generate audio
    print("Step 4/4 -- Generating audio...")
    audio_path = str(output_dir / f"{timestamp}_episode.mp3")
    pace = "energetic" if args.tone == "energetic" else "meditative"
    generate_audio(script, audio_path, voice_key=args.voice, pace=pace)

    print(f"\n  Done! Your episode is ready:")
    print(f"  {audio_path}\n")


def main():
    parser = argparse.ArgumentParser(description="YouTube -> Meditative Audio Pipeline")
    parser.add_argument("url", help="YouTube channel, playlist, or video URL")
    parser.add_argument("--videos", type=int, default=8)
    parser.add_argument("--voice", default="ryan", choices=list(VOICES.keys()))
    parser.add_argument("--length", type=int, default=40, choices=[20, 40, 60, 80])
    parser.add_argument("--tone", default="contemplative", choices=["contemplative", "philosophical", "energetic"])
    parser.add_argument("--after", default=None, help="Only videos after YYYYMMDD")
    parser.add_argument("--output", default=str(Path.home() / "audio_episodes"))
    parser.add_argument("--script-only", action="store_true", help="Generate script text only, no audio")
    args = parser.parse_args()

    run_pipeline(args)


if __name__ == "__main__":
    main()
