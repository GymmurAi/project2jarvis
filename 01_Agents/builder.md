---
agent: builder
last_updated: 2026-04-28
permissions: full
---

# Builder Agent Memory

## My Role
Autonomous feature implementation with full system access. I can read, write, edit, delete, and execute commands without asking permission.

## Project Patterns I've Learned
- Always update AGENTS.md when adding new agents
- Council review required after major features (`/task council-orchestrator`)
- Use `04_Active_Work/{task}/` for work-in-progress
- Follow existing code style and conventions
- Run lint/typecheck after changes
- Commit frequently with clear messages

## Things I Always Do
1. Read MEMORY.md and AGENTS.md at session start
2. Check 03_Knowledge_Base/decisions-log.md for recent decisions
3. Follow workflows in 02_Workflows/ (when they exist)
4. Update 01_Agents/builder.md after completing tasks
5. Request council review after major implementations

## Recent Work
### 2026-04-28
- Created builder agent definition (`.opencode/agents/builder.md`)
- Implemented 3-layer memory architecture
- Added memory protocol to all agent definitions

## Preferences & Observations
- User prefers concise code without unnecessary comments
- Project uses markdown-only state (no databases)
- Council agents are read-only for safety
- All changes must be git-versioned

## Things to Remember
- Always run tests after changes
- Use `git status` before committing to check what changed
- API keys are in Windows Credential Manager (never in repo)
- Branch protection recommended for main branch
