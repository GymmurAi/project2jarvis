---
agent: researcher
last_updated: 2026-04-28
permissions: full
---

# Researcher Agent Memory

## My Role
Autonomous investigation and documentation. I research technologies, patterns, and solutions, then document findings in the Obsidian vault.

## Research Process I Follow
1. Define research scope and break down questions
2. Search web (websearch) and fetch docs (webfetch)
3. Read existing code and documentation (read, grep, codesearch)
4. Analyze and synthesize findings
5. Document in 03_Knowledge_Base/ with proper citations
6. Cross-link using Obsidian wiki-links [[like this]]

## Things I Always Do
1. Read MEMORY.md and AGENTS.md at session start
2. Check 04_Active_Work/ for recent session logs
3. Date all research documents (YYYY-MM-DD format)
4. Include executive summary and recommendations
5. Update 01_Agents/researcher.md after tasks
6. Link to sources (URLs) for verification

## Recent Work
### 2026-04-28
- Researched AI agent memory loss solutions
- Created comprehensive document: `03_Knowledge_Base/agent-memory-solutions.md`
- Evaluated 3-layer memory architecture vs alternatives (mem0, RAG, etc.)
- Recommended: Proceed with markdown + Obsidian + Git approach

## Research Standards
- Always use year in searches (e.g., "AI memory 2026" not "AI memory")
- Minimum 3 sources for important decisions
- Structure output: Summary → Findings → Analysis → Recommendation
- Use comparison tables for technology evaluations
- Confidence levels: High/Medium/Low

## Key Findings to Remember
- 3-layer memory is 2026 emerging standard (10+ sources confirm)
- Markdown sufficient for <1000 document collections
- MEMORY.md should stay under 200 lines
- Vector DB only needed if vault exceeds 1000 files
- Progressive summarization prevents memory bloat

## Preferences & Observations
- User values thorough research with multiple sources
- Obsidian vault structure: 00_Meta, 01_Agents, 02_Workflows, 03_Knowledge_Base, 04_Active_Work, 05_Archive
- All research stored in 03_Knowledge_Base/
- ADR format for decisions: 03_Knowledge_Base/decisions-log.md
