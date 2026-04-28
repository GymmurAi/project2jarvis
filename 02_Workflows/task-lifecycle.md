# Task Lifecycle Workflow

Standard process for executing tasks in Project2Jarvis.

---

## Overview

Every task should follow this lifecycle:
```
Create → Assign → Execute → Review → Complete → Archive
```

---

## Step 1: Create Task

### 1.1 Define Task
- Create folder: `04_Active_Work/{task-name}/`
- Create `README.md` with:
  - Task description
  - Acceptance criteria
  - Dependencies
  - Assigned agent

### 1.2 Choose Agent
| Task Type | Agent to Use |
|-----------|---------------|
| New feature | `/task builder` |
| Research | `/task researcher` |
| Maintenance | `/task maintainer` |
| Review | `/task council-orchestrator` |
| Architecture | Switch to `council-system-architect` |

---

## Step 2: Execute Task

### 2.1 Session Start (Agent Does This)
1. Read `MEMORY.md`
2. Read `AGENTS.md`
3. Read `03_Knowledge_Base/decisions-log.md`
4. Check `04_Active_Work/{task-name}/`

### 2.2 During Execution
- Follow memory protocol (update agent-specific memory)
- Create session log: `04_Active_Work/session-YYYY-MM-DD.md`
- Commit work-in-progress if needed

### 2.3 Quality Checks
- Run linter: `npm run lint` (or equivalent)
- Run typecheck: `npm run typecheck` (or equivalent)
- Run tests: `npm test` (or equivalent)

---

## Step 3: Review

### 3.1 Self-Review
Agent checks:
- [ ] Acceptance criteria met?
- [ ] Tests passing?
- [ ] Documentation updated?
- [ ] Code follows conventions?

### 3.2 Council Review (For Major Changes)
```
/task council-orchestrator
Review the implementation in @04_Active_Work/{task-name} for security, performance, and quality.
```

Council members automatically invoked:
- @council-security - Security review
- @council-performance - Performance review
- @council-quality - Code quality review
- @council-docs - Documentation review

### 3.3 Address Feedback
- Fix issues identified by council
- Re-run tests
- Update documentation

---

## Step 4: Complete Task

### 4.1 Final Verification
- [ ] All tests pass
- [ ] Lint/typecheck clean
- [ ] Documentation complete
- [ ] Council review passed (if applicable)

### 4.2 Update Memory
1. Update `MEMORY.md` with completed task (keep <200 lines)
2. Log decision in `03_Knowledge_Base/decisions-log.md` (ADR format)
3. Update agent memory in `01_Agents/{agent}.md`

### 4.3 Commit
```bash
git add .
git commit -m "feat: complete {task-name}

- [bullet point 1]
- [bullet point 2]
- Reviewed by: council-orchestrator"
```

---

## Step 5: Archive

### 5.1 Move to Archive
```bash
mv 04_Active_Work/{task-name} 05_Archive/{task-name}
git add .
git commit -m "archive: {task-name}"
```

### 5.2 Update Logs
- Ensure session log exists: `04_Active_Work/session-YYYY-MM-DD.md`
- Add to `03_Knowledge_Base/lessons-learned.md` if new insights

---

## Task Template

Create `04_Active_Work/{task-name}/README.md`:

```markdown
# Task: {Task Name}

**Created**: YYYY-MM-DD  
**Agent**: {builder/researcher/maintainer}  
**Status**: In Progress / Complete / Archived

---

## Description
[What needs to be done]

---

## Acceptance Criteria
- [ ] Criteria 1
- [ ] Criteria 2
- [ ] Criteria 3

---

## Dependencies
- [Dependency 1]
- [Dependency 2]

---

## Notes
[Progress notes, decisions made, etc.]
```

---

## Quick Reference

| Step | Action | File/Folder |
|------|--------|-------------|
| Create | Define task | `04_Active_Work/{task}/README.md` |
| Execute | Do the work | `04_Active_Work/{task}/*` |
| Log | Session log | `04_Active_Work/session-YYYY-MM-DD.md` |
| Review | Council review | Invoke `@council-orchestrator` |
| Complete | Update memory | `MEMORY.md`, `01_Agents/*.md` |
| Commit | Git commit | Repository root |
| Archive | Move to archive | `05_Archive/{task}/` |
