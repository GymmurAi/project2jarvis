# Research: Claude Code vs Project2Jarvis Agent Architecture Comparison

## Executive Summary

This research compares the agent architecture of Claude Code (Anthropic's official AI coding assistant) with our Project2Jarvis multi-agent system. Both systems use markdown-based agent definitions stored in dedicated directories, but Claude Code has more advanced multi-agent coordination features including experimental "Agent Teams" with peer-to-peer messaging and git worktree isolation. Our Project2Jarvis system is simpler but fully operational, using a parent-child subagent model without nested agent spawning.

**Key Finding**: The fundamental architecture is nearly identical (file-based agent definitions, skills system, rules files), but Claude Code has native experimental features for true multi-agent coordination that we currently lack.

## Research Questions

1. How does Claude Code structure agent definitions compared to Project2Jarvis?
2. What multi-agent coordination patterns does Claude Code support?
3. How do skills and documentation differ between the two systems?
4. What experimental features exist in Claude Code that we don't have?
5. What can we learn from Claude Code's approach?

## Findings

### Source 1: Claude Code Agent Teams Documentation
- **URL**: https://aifreeapi.com/en/posts/claude-code-agent-teams
- **Date Accessed**: 2026-05-01
- **Key Points**:
  - Agent Teams shipped as experimental feature in February 2026
  - Enables peer-to-peer coordination between Claude Code sessions
  - Uses `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=true` feature flag
  - Requires Claude Code v2.1.32 or later
  - Anthropic used 16 parallel agents to build a 100,000-line C compiler (~$20,000 cost, 2,000 sessions)
- **Relevance**: High - Shows Claude Code's production multi-agent capabilities

### Source 2: TeammateTool Reverse Engineering
- **URL**: https://gist.github.com/kieranklaassen/d2b35569be2c7f1412c64861a219d51f
- **Date Accessed**: 2026-05-01
- **Key Points**:
  - TeammateTool found in Claude Code v2.1.19 binary via `strings` analysis
  - 13 operations: spawnTeam, discoverTeams, requestJoin, approveJoin, rejectJoin, write, broadcast, requestShutdown, approveShutdown, rejectShutdown, approvePlan, rejectPlan, cleanup
  - File-based coordination: `~/.claude/teams/{team-name}/` and `~/.claude/tasks/{team-name}/`
  - Environment variables: `CLAUDE_CODE_TEAM_NAME`, `CLAUDE_CODE_AGENT_ID`, `CLAUDE_CODE_AGENT_TYPE`
  - Feature flags: `I9() && qFB()` must return true
- **Relevance**: High - Reveals internal architecture of Claude Code's multi-agent system

### Source 3: OpenCode Agent Documentation
- **URL**: https://open-code.ai/en/docs/agents
- **Date Accessed**: 2026-05-01
- **Key Points**:
  - OpenCode supports same markdown agent format as Claude Code
  - Agent storage: `~/.config/opencode/agents/` (global) and `.opencode/agents/` (project)
  - Claude Code equivalent: `~/.claude/agents/` and `.claude/agents/`
  - Same frontmatter format: description, mode, model, temperature, tools, permission
  - Skills stored in `skills/` subdirectories with `SKILL.md`
- **Relevance**: High - Confirms architectural parity between systems

### Source 4: forge-council Plugin
- **URL**: https://github.com/N4M3Z/forge-council
- **Date Accessed**: 2026-05-01
- **Key Points**:
  - Third-party multi-agent council system for Claude Code
  - 13 markdown agent files + 5 skills
  - 3-round debate structure: initial positions → challenges → convergence
  - Council skills: `/DeveloperCouncil`, `/DebateCouncil`, `/ProductCouncil`, `/KnowledgeCouncil`
  - Pure markdown orchestration (no compiled code)
- **Relevance**: Medium - Shows community extending Claude Code's agent system

### Source 5: Agent Tower Plugin
- **URL**: https://github.com/bayramannakov/agent-tower-plugin
- **Date Accessed**: 2026-05-01
- **Key Points**:
  - Multi-agent deliberation: council, debate, deliberation modes
  - Supports multiple AI backends: Claude, Codex, Gemini
  - Council mode: parallel agents → anonymous ranking → chairman synthesis
  - Debate mode: adversarial two-agent debate with judge
  - Deliberation mode: producer/reviewer iteration loop
- **Relevance**: Medium - Alternative multi-agent pattern for Claude Code

### Source 6: Agent Teams Guide (Claudio Novaglio)
- **URL**: https://www.claudio-novaglio.com/en/papers/agent-teams-claude-code-multi-agent-orchestration
- **Date Accessed**: 2026-05-01
- **Key Points**:
  - Agent Teams = 4 components: Team Lead, Teammates, Task List, Mailbox
  - Subagents vs Teammates: subagents report to parent only, teammates do peer-to-peer
  - Git worktree isolation: each teammate works on separate copy of repository
  - Token cost scales linearly with number of teammates
  - CLAUDE.md loaded by all agents (consistency in conventions)
- **Relevance**: High - Detailed operational understanding of Claude Code's system

## Analysis

### Architecture Comparison Table

| Feature | Claude Code | Project2Jarvis (OpenCode) |
|---------|-------------|---------------------------|
| **Agent Definition Format** | Markdown with YAML frontmatter | Markdown with YAML frontmatter |
| **Agent Storage (Project)** | `.claude/agents/` | `.opencode/agents/` |
| **Agent Storage (Global)** | `~/.claude/agents/` | `~/.config/opencode/agents/` |
| **Rules/Instructions File** | `CLAUDE.md` | `AGENTS.md` (supports both) |
| **Skills System** | `.claude/skills/*/SKILL.md` | `.opencode/skills/*/SKILL.md` |
| **Subagent Spawning** | Task tool (parent→child only) | Task tool (parent→child only) |
| **Nested Subagents** | Not allowed (hard constraint) | Not allowed (same constraint) |
| **Peer-to-Peer Agents** | Yes (Agent Teams, experimental) | No |
| **Inter-Agent Messaging** | SendMessage tool (Agent Teams) | No native messaging |
| **Shared Task Lists** | `~/.claude/tasks/` (Agent Teams) | `04_Active_Work/` + audit logs |
| **Git Isolation** | Worktree per agent (Agent Teams) | Single branch per agent |
| **Coordination State** | Filesystem + messaging | Task files + audit logs |
| **Feature Flag Control** | Yes (experimental features) | No (all features enabled) |

### Agent Types Comparison

| Type | Claude Code | Project2Jarvis |
|------|-------------|----------------|
| **Primary Agent** | Main interactive session | Main interactive session |
| **Subagent** | Task tool spawn, reports to parent, isolated context | Task tool spawn, reports to parent, isolated context |
| **Teammate** | Independent session, peer-to-peer (experimental) | N/A |
| **Council Member** | Via plugins (forge-council, agent-tower) | Native council agents |

### Multi-Agent Patterns in Claude Code

#### 1. Subagent Pattern (Production-Ready)
```
Parent Agent
    ├── Subagent 1 (Task tool)
    ├── Subagent 2 (Task tool)
    └── Subagent 3 (Task tool)
```
- Parallel execution via multiple Task tool calls
- Each subagent has separate context window
- Results synthesized by parent
- Cannot spawn nested subagents

#### 2. Agent Teams Pattern (Experimental)
```
Team Lead (spawns and coordinates)
    ├── Teammate 1 (independent session)
    ├── Teammate 2 (independent session)
    └── Teammate 3 (independent session)

Coordination:
- Shared task list: ~/.claude/tasks/{team}/
- Peer-to-peer messages: SendMessage tool
- Mailbox: ~/.claude/teams/{team}/messages/
```
- True peer-to-peer coordination
- Git worktree isolation
- Enabled via feature flag

#### 3. Council Pattern (Plugin-Based)
```
Arbiter/Chairman
    ├── Domain Expert 1 (e.g., Security)
    ├── Domain Expert 2 (e.g., Performance)
    ├── Domain Expert 3 (e.g., UX)
    └── Domain Expert 4 (e.g., Legal)

Process:
1. Broadcast question to all experts
2. Collect independent responses
3. Synthesize final recommendation
```
- Multiple perspectives on single question
- Anonymous ranking in some implementations
- Arbiter/chairman synthesizes final answer

## Key Insights

### 1. Architectural Parity
Both systems use nearly identical file-based agent definitions. The transition from Claude Code to OpenCode (or vice versa) would be straightforward for agent files.

### 2. Coordination Gap
Claude Code's experimental Agent Teams feature provides true peer-to-peer coordination that we lack. Our system uses a hierarchical parent-child model exclusively.

### 3. Git Isolation Advantage
Claude Code's use of git worktrees for Agent Teams prevents file conflicts when multiple agents modify the same repository. We use separate branches (`agent/builder`, etc.) but lack true worktree isolation.

### 4. Plugin Ecosystem
Third-party plugins (forge-council, agent-tower) extend Claude Code's capabilities significantly. Our council system is native but less battle-tested.

### 5. Production Validation
Anthropic's use of 16 parallel agents to build a C compiler demonstrates the production viability of their approach. Cost: ~$20,000 across 2,000 sessions.

## Recommendations

### Short Term (No Code Changes)
1. **Document our architecture clearly** - Ensure AGENTS.md accurately reflects our current capabilities
2. **Adopt worktree best practices** - Even without native support, document how to use git worktrees manually for parallel agent work
3. **Standardize agent memory** - Complete the `01_Agents/` working memory files for all 19 agents (currently only ~7 have them)

### Medium Term (Consider Implementation)
1. **Evaluate Agent Teams pattern** - Consider implementing peer-to-peer coordination similar to Claude Code's TeammateTool
2. **Add inter-agent messaging** - A simple filesystem-based message passing system could enable teammate-style coordination
3. **Git worktree integration** - Automate worktree creation for parallel agent sessions

### Long Term (Research)
1. **Cost optimization** - Study Claude Code's token usage patterns for multi-agent coordination
2. **Plugin system** - Consider allowing third-party agent plugins like forge-council
3. **Nested agents** - Evaluate if nested subagent spawning would be valuable (currently prohibited in both systems)

## Implementation Notes

If we decide to implement Agent Teams-style coordination:

1. **File Structure** (mimicking Claude Code):
   ```
   .opencode/
   ├── teams/
   │   └── {team-name}/
   │       ├── config.json
   │       └── messages/
   └── tasks/
       └── {team-name}/
   ```

2. **Environment Variables**:
   - `OPENCODE_TEAM_NAME`
   - `OPENCODE_AGENT_ID`
   - `OPENCODE_AGENT_TYPE`

3. **New Tools Needed**:
   - `spawnTeammate` - Create independent agent session
   - `sendMessage` - Peer-to-peer messaging
   - `broadcastMessage` - Send to all teammates
   - `readMessages` - Check mailbox

4. **Git Worktree Integration**:
   ```bash
   git worktree add ../agent-worktrees/{agent-name} -b agent/{agent-name}
   ```

## Open Questions

1. Should we implement peer-to-peer agent coordination, or is hierarchical parent-child sufficient?
2. What's the optimal token budget for multi-agent coordination?
3. How can we prevent agent conflicts without worktree isolation?
4. Should we build a plugin system like forge-council, or keep agents native?

## Sources

1. [Claude Code Agent Teams Guide](https://aifreeapi.com/en/posts/claude-code-agent-teams) - AI Free API Team, 2026-03-17
2. [Claude Code Hidden Multi-Agent System](https://gist.github.com/kieranklaassen/d2b35569be2c7f1412c64861a219d51f) - kieranklaassen, 2026-01-23
3. [OpenCode Agents Documentation](https://open-code.ai/en/docs/agents) - OpenCode Docs
4. [forge-council Plugin](https://github.com/N4M3Z/forge-council) - N4M3Z, 2026-02-16
5. [Agent Tower Plugin](https://github.com/bayramannakov/agent-tower-plugin) - bayramannakov, 2026-01-21
6. [Agent Teams in Claude Code](https://www.claudio-novaglio.com/en/papers/agent-teams-claude-code-multi-agent-orchestration) - Claudio Novaglio, 2026-03-16
7. [Claude Code Agentic Engineering](https://www.jayminwest.com/agentic-engineering-book/10-practitioner-toolkit/1-claude-code) - Jaymin West
8. [OpenCode Config Documentation](https://open-code.ai/docs/en/config) - OpenCode Docs
9. [Agent Configuration | OpenCode Guide](https://opencodeguide.com/en/docs/configure/agents/) - OpenCode Guide

## Metadata

- **Date**: 2026-05-01
- **Researcher**: @researcher
- **Confidence**: High
- **Tags**: `#architecture` `#multi-agent` `#claude-code` `#opencode` `#comparison`
- **Related Research**: `03_Knowledge_Base/agent-memory-solutions.md`, `00_Meta/ARCHITECTURE.md`

## Change Log

| Date | Change |
|------|--------|
| 2026-05-01 | Initial research and documentation |
