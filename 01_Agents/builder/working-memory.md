# Builder Agent Working Memory

*Last updated: 2026-05-01 by @builder*

---

## Current Context

- **Project**: Project2Jarvis (OpenCode AI Agency System)
- **Branch**: agent/builder
- **Model**: opencode/big-pickle
- **Permissions**: FULL ACCESS (edit:allow, bash:allow, external_dir:allow)

---

## Recent Tasks Completed

| Date | Task | Status |
|------|------|--------|
| 2026-05-01 | Implemented oh-my-opencode-dashboard integration | COMPLETED |
| 2026-05-01 | Installed Bun runtime v1.3.13 on Windows | COMPLETED |
| 2026-05-01 | Created launch-dashboard.ps1 script | COMPLETED |
| 2026-05-01 | Committed Plan Agent work to `feat/plan-agent` | COMPLETED |
| 2026-05-01 | Fixed P0 issues (ADR-013-018) for Plan Agent | COMPLETED |
| 2026-05-01 | Created PR #1 via GitHub API | COMPLETED |
| 2026-04-30 | Implemented agency-agents (code-reviewer, mcp-builder, etc.) | COMPLETED |
| 2026-04-29 | Executive Command Center implementation | COMPLETED |

---

## Implementation Patterns Learned

### Bun on Windows
- **Install command**: `powershell -c "irm bun.sh/install.ps1|iex"`
- **Install location**: `C:\Users\$env:USERNAME\.bun\bin\bun.exe`
- **Version pinned**: >=1.3.5 (security recommendation)
- **Verify install**: `bun --version` (must add to PATH or use full path)
- **bunx usage**: `bunx package@latest -- --arg` (note double `--` for args)

### oh-my-opencode-dashboard Integration
- **Tech stack**: Bun + Hono (API) + React (UI) + Vite (build)
- **Launch**: `bunx oh-my-opencode-dashboard@latest -- --project /path`
- **Register source**: `bunx oh-my-opencode-dashboard@latest add --name "Project" --project /path`
- **Health check**: `curl http://127.0.0.1:51234/api/health` → `{"ok":true}`
- **API endpoints**:
  - `/api/health` - Health check
  - `/api/dashboard` - Full dashboard state (sessions, tasks, tokens, time series)
- **Security**: Dashboard is READ-ONLY, never exposes prompts/tool args/raw outputs
- **Default port**: 51234 (configurable with `--port`)
- **Bind host**: 127.0.0.1 only (local-only, secure by default)

### Windows Path Handling
- **PowerShell**: Use `;` for PATH separation, not `:`
- **Invoke-WebRequest**: Must use `-UseBasicParsing` flag
- **Process management**: `Get-Process -Name "bun" | Stop-Process -Force`
- **Background processes**: `Start-Process -WindowStyle Hidden` for long-running tasks

---

## Dashboard Integration Notes

### What Works
- ✅ Bun v1.3.13 installed and verified
- ✅ Dashboard launches via `bunx` without global install
- ✅ Project2Jarvis registered as source (ID: 8f097b58...)
- ✅ API returns real data (sessions, background tasks, token usage)
- ✅ Security verified: no sensitive data exposed in API responses
- ✅ launch-dashboard.ps1 script created with start/stop/status commands

### Known Behaviors
- Dashboard uses OpenCode's local storage (typically `%LOCALAPPDATA%\opencode`)
- Source registration is persistent (stored in OpenCode config)
- `bunx` downloads package on each run (can be slow on first launch)
- Dashboard binds to 127.0.0.1 only (not accessible from other machines)

### Future Enhancements
- Consider global install (`bun add -g oh-my-opencode-dashboard`) for faster startup
- Add dashboard URL to AGENTS.md Quick Start section
- Potentially fork for custom theming (only if ui-ux-pro-max requests extensive changes)
- Add dashboard status to daily-dashboard.md generation

---

## Code Patterns

### PowerShell Scripts
```powershell
# Always use param block for script arguments
param(
    [string]$Param1,
    [switch]$Flag
)

# Use $ErrorActionPreference = "Stop" for strict error handling
$ErrorActionPreference = "Stop"

# Check command existence
if (-not (Test-Path $Path)) {
    Write-Host "Error: Path not found" -ForegroundColor Red
    exit 1
}
```

### Git Workflow (Builder Agent)
- Branch: `agent/builder`
- Commit message format: `feat: description` or `fix: description`
- Always run lint/typecheck before commit
- Request council review (@council-orchestrator) after major features

---

## Things to Remember

1. **ADR-002**: Use OpenCode native features only, no custom frameworks
2. **ADR-004**: All state in markdown, git-versioned
3. **Session protocol**: Read working memory → Do work → Update working memory
4. **Audit logging**: Log all actions to `06_Audit_Logs/audit-YYYY-MM-DD.md`
5. **Council review**: Major features need review before merge to main

---

## Active Issues / TODO

- [ ] Test dashboard with multiple concurrent sessions
- [ ] Verify dashboard works after OpenCode updates
- [ ] Consider adding dashboard launch to OpenCode startup hooks
- [ ] Document dashboard customization options (if forked)

---

*This file is my per-agent working memory. Update after each task.*
