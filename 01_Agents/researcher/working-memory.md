# Researcher Working Memory

*Last updated: 2026-04-30 by @researcher (agency-agents Evaluation)*

## Current Task Context
- **Status**: Available
- **Current Task**: None
- **Active Branch**: agent/researcher

## Researcher-Specific Patterns Learned
- Always read MEMORY.md, AGENTS.md, decisions-log.md at session start
- Follow ADR-002: Use native OpenCode features only
- Follow ADR-003: Full access agent, use with caution
- Research documents go to 03_Knowledge_Base/
- **Tool Selection Guide**:
  - Use `websearch` to discover URLs on a topic (fast, ~0.5s)
  - Use `webfetch` for quick static page reads (basic markdown)
  - Use `Crawl4AI` for JS-rendered content, clean LLM-ready markdown, multi-page crawling
- Cite sources in research documents

## Crawl4AI Integration (2026-04-30)
- **Installed**: `pip install crawl4ai` (v0.8.x)
- **MCP Config**: Configured in `opencode.json` but tools not appearing (use direct Python as workaround)
- **Key Features**:
  - `AsyncWebCrawler.arun()` - Single page scrape with JS rendering
  - `AsyncWebCrawler.arun_many()` - Multi-page concurrent crawling
  - Clean markdown output (67% token reduction vs HTML)
  - Browser automation via Playwright (headless mode supported)
- **Usage Pattern**: 
  1. Use `websearch` to find URLs
  2. Use Crawl4AI (via Python) to extract clean markdown
  3. Document findings in `03_Knowledge_Base/`
- **Windows Note**: Fix Unicode encoding with `sys.stdout.reconfigure(encoding='utf-8')`

## agency-agents Evaluation (2026-04-30)
- **Repository**: https://github.com/msitarzewski/agency-agents
- **Stats**: 144+ agents, 12+ divisions, 14.5k GitHub stars, MIT License
- **Key Finding**: Comprehensive AI agent library with strong personality-driven agents
- **OpenCode Integration**: Native support via `.opencode/agents/` directory
- **Relevant Agents for Project2Jarvis**:
  - HIGH: Code Reviewer, Security Engineer, Evidence Collector, MCP Builder
  - MEDIUM: UI Designer, Reality Checker, Workflow Architect
- **Recommendation**: Selective adoption - keep our council system, adopt 5-10 high-value agents
- **Research Document**: `03_Knowledge_Base/agency-agents-evaluation.md`
- **Integration Method**: Use `./scripts/install.sh --tool opencode` from agency-agents repo

## Recent Work
- Agent memory solutions research (see 03_Knowledge_Base/agent-memory-solutions.md)
- UI/UX research for Executive Command Center
- Crawl4AI integration research (see 03_Knowledge_Base/crawl4ai-research.md)
- **agency-agents evaluation** (see 03_Knowledge_Base/agency-agents-evaluation.md)
- **Claude Code vs Project2Jarvis architecture comparison** (see 03_Knowledge_Base/claude-code-vs-project2jarvis-agent-architecture.md)
- **Plan Agent research & creation** (see 03_Knowledge_Base/plan-agent-research.md)
  - Analyzed GitHub repo: Jeomon/Plan-Agent-with-Meta-Agent
  - Deep analysis of past failures (Three.js crash, Exec Command Center rejection)
  - Designed 6-phase planning process
  - Built Plan Agent with failure prevention rules
  - Created working memory, planning template, knowledge base doc
  - Updated AGENTS.md and active-registry.md (20 agents total)

## Things to Remember
- All API keys in Windows Credential Manager (never in repo)
- Create feature branches, never commit directly to main (ADR-010)
- Log all actions to 06_Audit_Logs/audit-YYYY-MM-DD.md
- Research files: Use YAML frontmatter with tags for future RAG indexing
- **Crawl4AI Research Workflow**: websearch (find URLs) → Crawl4AI (extract content) → document (03_Knowledge_Base/)
- **agency-agents**: Can adopt selectively using `agency-*` prefix to avoid conflicts
- **Claude Code Architecture Insights**:
  - Both systems use identical markdown-based agent definitions
  - Claude Code has experimental "Agent Teams" with peer-to-peer coordination
  - Git worktree isolation prevents file conflicts in parallel agent work
  - Our system is simpler but fully operational (no feature flags)
  - Consider worktree best practices for parallel agent sessions

## Quick Reference
- **Start**: Read AGENTS.md → MEMORY.md → decisions-log.md → this file
- **End**: Update this file, create session log, add research to 03_Knowledge_Base/
- **Branch**: Always use `agent/researcher` branch, merge to main after council review
- **agency-agents**: Clone repo → convert.sh → install.sh --tool opencode → test @agent-name
