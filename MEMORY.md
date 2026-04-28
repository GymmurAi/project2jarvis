# Working Memory

*Last updated: 2026-04-28 by researcher*

## Project Context
- **Project**: Project2Jarvis (OpenCode + Obsidian multi-agent AI agency)
- **Tech stack**: OpenCode AI agents, Obsidian vault, Git versioning
- **Architecture**: Council system (review agents) + Autonomous agents (builder/researcher/maintainer)

## Key Decisions Made
- [2026-04-28] Adopted 3-layer memory architecture (session/working/permanent)
- [2026-04-28] Using markdown files for memory (no vector DB yet - may add later)
- [2026-04-28] Council agents are read-only (edit:deny) for safety
- [2026-04-28] Autonomous agents (builder/researcher/maintainer) have FULL ACCESS

## Active Tasks
- [completed] Built web dashboard with dark theme & neon accents
- [completed] Fetched weather via wttr.in API (Wolverhampton, 12°C sunny)
- [completed] Created daily dashboard (markdown + HTML)
- [completed] Listed all 10 agents with status
- [pending] Create GitHub test repository (need gh CLI or MCP token)
- [pending] Set up automated session logging in 04_Active_Work/

## Things to Remember
- All API keys in Windows Credential Manager (never in repo)
- Git versioning for all markdown files
- Council agents: @council-security, @council-performance, @council-quality, @council-docs
- Autonomous agents: /task builder, /task researcher, /task maintainer
- Switch primary agents with Tab key
- Session logs: 04_Active_Work/session-YYYY-MM-DD.md

## Project Structure (Memory-Relevant)
```
00_Meta/              # AGENTS.md, MEMORY.md (this file), ARCHITECTURE.md
01_Agents/            # Agent-specific memory files
02_Workflows/         # Procedural memory (checklists)
03_Knowledge_Base/    # Semantic memory (research, decisions, lessons)
04_Active_Work/       # Episodic memory (session logs, tasks)
05_Archive/           # Old/completed work
```

## Recent Lessons Learned
- Previous AI agencies broke due to: no version control, shared state, over-engineering
- Solution: Simple markdown + Git + Native OpenCode features (no custom frameworks)
- Memory loss happens due to: context window limits, session restarts
- Fix: Persistent markdown files that agents read at session start
- MCP servers need tokens: GitHub MCP requires GITHUB_PERSONAL_ACCESS_TOKEN
- Weather APIs (wttr.in) provide rich JSON data perfect for dashboards
- Dark themes with neon accents (#00dbde, #fc00ff) look amazing

## Tools Built (2026-04-28)
- **auto-summary.py**: Memory management script at `.opencode/scripts/auto-summary.py`
  - Checks MEMORY.md line count, auto-summarizes if >200 lines
  - Keeps 40% most important content (scored by keywords, headers, recency)
  - Archives old content to `03_Knowledge_Base/lessons-learned.md`
  - Features: color output, memory health score, progress bars, spinners
- **MCP servers configured**: github and fetch (mcp-fetch-server) in `~/.opencode/mcp.json`

## Quick Reference
- **Start session**: Read AGENTS.md → MEMORY.md → 03_Knowledge_Base/decisions-log.md
- **End session**: Update MEMORY.md (<200 lines), append to session log, update knowledge base
- **Agent naming**: Council agents use `council-*` prefix, autonomous agents are standalone
