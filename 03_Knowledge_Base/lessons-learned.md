# Lessons Learned

*Accumulated insights from building and breaking AI agencies*

---

## Technical Lessons

### Memory & State
- **Lesson**: AI agents lose context on session restart
  - **Solution**: Persistent markdown files (MEMORY.md, session logs)
  - **Date**: 2026-04-28
  - **Source**: Research on agent-memory-solutions.md

- **Lesson**: Context window limits cause truncation of important info
  - **Solution**: 3-layer memory architecture, progressive summarization
  - **Date**: 2026-04-28

### Architecture
- **Lesson**: Custom frameworks break over time (maintenance burden)
  - **Solution**: Use native OpenCode features only
  - **Date**: 2026-04-28

- **Lesson**: Shared state between agents causes conflicts
  - **Solution**: Isolated task folders (04_Active_Work/{task}/)
  - **Date**: 2026-04-28

### Security
- **Lesson**: API keys in repo = compromised accounts
  - **Solution**: Windows Credential Manager, .gitignore for .env
  - **Date**: 2026-04-28
  - **Severity**: Critical

- **Lesson**: Unrestricted agents can escape project root
  - **Solution**: OpenCode permissions (external_directory: deny)
  - **Date**: 2026-04-28

---

## Workflow Lessons

### Task Management
- **Lesson**: Unclear task definitions lead to agent confusion
  - **Solution**: Standardized workflows in 02_Workflows/, clear task descriptions
  - **Date**: 2026-04-28

- **Lesson**: No review process = accumulated tech debt
  - **Solution**: Council review after major changes (council-orchestrator)
  - **Date**: 2026-04-28

### Documentation
- **Lesson**: Outdated docs cause agents to make wrong assumptions
  - **Solution**: Documentation updates as part of every task
  - **Date**: 2026-04-28

---

## Template for New Lessons

```
- **Lesson**: [What went wrong or was discovered]
  - **Solution**: [How to handle it]
  - **Date**: YYYY-MM-DD
  - **Source**: [Where this came from]
  - **Severity**: Critical/High/Medium/Low (optional)
```
