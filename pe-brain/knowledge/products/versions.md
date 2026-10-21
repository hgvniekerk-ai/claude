---
id: prod-versions
title: Product and tag version register
domain: products
type: register
authority: unverified
owner: "[TBC]"
reviewed: ""
sources:
  - "[TBC: release records in s3-agent-knowledge-base or the product team]"
tags: [versions, products, tags, register]
---

# Product and tag version register

`pe.py check` warns when a project record lists `product@version` that is not in this table. That is the version-awareness mechanism: projects declare what is installed, this register says what exists and what is current.

| product | version | status | tag_schema | released | notes | source |
|---|---|---|---|---|---|---|
| [TBC] | | | | | | [TBC] |

`status`: current, supported, retired. `tag_schema`: the tag list or tag naming version the product expects, if versioned.
