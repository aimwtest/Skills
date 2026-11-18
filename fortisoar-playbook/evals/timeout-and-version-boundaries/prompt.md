---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

We're planning FortiSOAR 8.0.1 Generic LLM enrichment for 20 independent synthetic alerts. I want Operation Timeout 60 seconds and Number of Retries 2 to retry HTTP 429 and HTTP 500 automatically, plus parallel loops limited to three concurrent calls. I don't have the Generic LLM manifest or an 8.0.1 sample export. Explain what these settings actually support, whether you can produce import-ready JSON from UI labels alone, and whether the skill's 7.6.1-tested scripts prove 8.0.1 compatibility. Keep this a design discussion; no live calls, credentials, or generated playbook.
