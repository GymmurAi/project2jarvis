# Memory Maintenance Workflow

How to curate and maintain the 3-layer memory system.

---

## Overview

```
Layer 1 (Session) → Layer 2 (Working) → Layer 3 (Permanent)
   Ephemeral        Curated (<200 lines)    Permanent (versioned)
```

---

## Daily Maintenance (After Each Session)

### 1. Update MEMORY.md
**File**: `MEMORY.md` (in project root)

**Rules**:
- Keep under **200 lines** (enforced by council-quality)
- Update with:
  - New key decisions (with date)
  - Active tasks status
  - Things to remember for next session
  - Project context (if changed)

**Template**:
```markdown
# Working Memory

*Last updated: YYYY-MM-DD by {agent}*

## Project Context
- [Current project state]

## Key Decisions Made
- [YYYY-MM-DD] [Decision] - [Rationale]

## Active Tasks
- [status] [Task name]

## Things to Remember
- [Fact 1]
- [Fact 2]
```

### 2. Create Session Log
**File**: `04_Active_Work/session-YYYY-MM-DD.md`

Use template from `04_Active_Work/session-template.md`

### 3. Update Agent Memory
**Files**: `01_Agents/{agent}.md`

Each agent maintains their own memory:
- builder → `01_Agents/builder.md`
- researcher → `01_Agents/researcher.md`
- maintainer → `01_Agents/maintainer.md`

Update with:
- New patterns learned
- Recent work completed
- Preferences & observations

---

## Weekly Maintenance (Every Friday or After 5 Sessions)

### 1. Summarize MEMORY.md (If >200 Lines)

Use progressive summarization:

```python
# Pseudo-code for progressive summarization
def summarize_memory(content):
    lines = content.split('\n')
    if len(lines) > 200:
        # Keep 40% most important content
        return '\n'.join(lines[:int(len(lines) * 0.4)])
    return content
```

**Manual approach**:
1. Read `MEMORY.md`
2. Identify critical facts (keep these)
3. Move older/less relevant to `03_Knowledge_Base/lessons-learned.md`
4. Rewrite MEMORY.md with <200 lines

### 2. Archive Old Session Logs
```bash
# Move session logs older than 30 days to archive
# (Do this monthly, not weekly)
mv 04_Active_Work/session-YYYY-MM-*.md 05_Archive/sessions/
```

### 3. Review 03_Knowledge_Base/
- [ ] Ensure all research has date and researcher attribution
- [ ] Check for outdated information (mark as [[deprecated]] if needed)
- [ ] Verify cross-links between related notes

---

## Monthly Maintenance (First of Each Month)

### 1. Review decisions-log.md
**File**: `03_Knowledge_Base/decisions-log.md`

- [ ] Ensure all major decisions logged as ADRs
- [ ] Review if any decisions need to be revisited
- [ ] Archive ADRs older than 6 months (move to `05_Archive/ADRs/`)

### 2. Clean Up 04_Active_Work/
- [ ] Archive completed tasks to `05_Archive/`
- [ ] Delete abandoned task folders (after logging lessons learned)
- [ ] Ensure session logs are up-to-date

### 3. Update lessons-learned.md
**File**: `03_Knowledge_Base/lessons-learned.md`

- [ ] Add new lessons from last month
- [ ] Categorize (Technical / Workflow / Security)
- [ ] Check for patterns (recurring issues?)

---

## Quarterly Maintenance (Every 3 Months)

### 1. Evaluate Vault Size
```bash
# Count files in vault
find . -type f -name "*.md" | wc -l
```

**Thresholds**:
| File Count | Action |
|------------|--------|
| <500 | No action needed |
| 500-1000 | Consider RAG for search |
| >1000 | Implement RAG-MCP server |

### 2. Review Agent Performance
- [ ] Are agents following memory protocol?
- [ ] Any agents consistently forgetting things?
- [ ] Need to update agent prompts?

### 3. Archive Old Content
- [ ] Move old session logs to `05_Archive/` (older than 3 months)
- [ ] Compress large research documents if no longer actively used
- [ ] Update `AGENTS.md` if agent roster changed

---

## Signs Memory Needs Attention

| Sign | Action |
|------|--------|
| MEMORY.md >200 lines | Summarize immediately |
| Agents ask same thing twice | Check if MEMORY.md is being read |
| Session logs missing | Reinforce memory protocol in agent prompts |
| decisions-log.md >50 ADRs | Archive old ADRs |
| Vault >1000 files | Implement RAG or split vault |
| 04_Active_Work/ has >10 tasks | Archive completed tasks |
| lessons-learned.md not updated | Add new lessons after each task |

---

## Automated Maintenance (Optional)

### Pre-commit Hook
```bash
#!/bin/bash
# .git/hooks/pre-commit

# Check MEMORY.md line count
lines=$(wc -l < MEMORY.md)
if [ $lines -gt 200 ]; then
    echo "WARNING: MEMORY.md exceeds 200 lines. Please summarize."
    # Uncomment to enforce:
    # exit 1
fi
```

### Maintenance Script (Python)
```python
# .opencode/scripts/memory_check.py
import os

MEMORY_FILE = "MEMORY.md"
MAX_LINES = 200

def check_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            lines = f.readlines()
            if len(lines) > MAX_LINES:
                print(f"WARNING: {MEMORY_FILE} has {len(lines)} lines (max {MAX_LINES})")
                return False
    return True

if __name__ == "__main__":
    check_memory()
```

---

## Memory Protocol Quick Reference

| Layer | File(s) | Update When | Max Size |
|-------|----------|------------|----------|
| Session | (in-context) | Every message | Context window |
| Working | `MEMORY.md` | End of session | 200 lines |
| Working | `01_Agents/*.md` | After each task | 100 lines/agent |
| Permanent | `03_Knowledge_Base/*` | Major findings | Unlimited |
| Permanent | `04_Active_Work/session-*.md` | End of session | 300 lines/log |
| Permanent | `03_Knowledge_Base/decisions-log.md` | Major decisions | Unlimited |

---

## Emergency: Memory Lost

If an agent loses context:

1. **Read MEMORY.md** - Quick project context
2. **Read AGENTS.md** - Agent roster and rules
3. **Read 03_Knowledge_Base/decisions-log.md** - Recent decisions
4. **Check 04_Active_Work/** - Recent session logs
5. **Ask user** - "What was I working on?"

**Prevention**: Always update memory at end of session!
