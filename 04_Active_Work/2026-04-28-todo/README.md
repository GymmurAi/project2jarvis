# TODO: Personal Development Coach - Production Hardening

**Date**: 2026-04-28  
**Status**: Pending - For Builder Agent  
**Session**: Next session  

---

## Critical Bugs to Fix (High Priority)

### 1. Strip ANSI Codes from Markdown Outputs
**Files**: `generate-report.ps1`, `attendance-monitor.ps1`, `ucas-reference-generator.ps1`  
**Issue**: ANSI escape codes (`[[32m`, `[[0m`) written to .md files, rendering them unreadable in standard viewers  
**Fix**: 
- Keep ANSI colors for terminal output only
- Write clean markdown (no ANSI) to .md files
- Add parameter: `-TerminalOutput` (default: false for files)

### 2. Replace Hardcoded Absolute Paths
**Files**: All 6 coaching scripts  
**Issue**: Hardcoded `D:\Projects\Project2Jarvis\...` breaks portability  
**Fix**:
- Use relative paths: `04_Active_Work/coaching-scripts/`
- Or config file: `college-config.json` with `BasePath`
- Update all `Out-File` paths to use relative/configurable paths

### 3. Fix UCAS Reference Script Bug
**File**: `ucas-reference-generator.ps1` (line ~156)  
**Issue**: Creates duplicate `.md.md` files via incorrect path concatenation  
**Fix**:
```powershell
# Wrong:
$outFile = "$outputDir\$studentName-ucas-ref-$date.md.md"

# Correct:
$outFile = "$outputDir\$studentName-ucas-ref-$date.md"
```

### 4. Add Automatic Directory Creation
**Files**: `1-to-1-session-log.ps1`, `set-targets.ps1`, `ucas-reference-generator.ps1`  
**Issue**: Scripts fail if `sessions/` or `ucas-refs/` folders don't exist  
**Fix**:
```powershell
$requiredDirs = @("sessions", "ucas-refs", "reports")
foreach ($dir in $requiredDirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
}
```

---

## Medium Priority Improvements

### 5. Update generate-report.ps1 to Read Real CSV
**File**: `generate-report.ps1`  
**Issue**: Currently uses hardcoded attendance data instead of reading `attendance.csv`  
**Fix**:
```powershell
# Replace hardcoded data with:
$attendance = Import-Csv $attendanceCsv
# Generate report from real data
```

### 6. Add Error Handling (try/catch)
**Files**: All 6 scripts  
**Issue**: No `try/catch` for CSV import errors, missing files  
**Fix**:
```powershell
try {
    $data = Import-Csv $csvPath
} catch {
    Write-Host "[[91mError reading CSV: $_[[0m"
    exit 1
}
```

### 7. Create Shared PowerShell Module
**File**: `04_Active_Work/coaching-scripts/CoachingTools.psm1`  
**Purpose**: Common functions for all scripts  
**Contents**:
- ANSI color functions (`Write-Color`, `Write-Success`, `Write-Warning`, `Write-Error`)
- Path management (`Get-CollegePath`, `Get-OutputPath`)
- Data validation (`Test-StudentData`, `Test-AttendanceRecord`)
- Report generation helpers (`New-AttendanceChart`, `New-ProprogressBar`)

### 8. Add Multi-Tenant Support
**File**: `college-config.json` (new file)  
**Purpose**: Configurable per college  
**Template**:
```json
{
  "collegeName": "Generic College",
  "basePath": "04_Active_Work/coaching-data/",
  "staff": {
    "headOfSchool": "Jane Smith",
    "programmeManager": "John Doe"
  },
  "policies": {
    "attendanceWarningThreshold": 85,
    "attendanceCriticalThreshold": 75,
    "maxTargetsPerStudent": 5
  },
  "misIntegration": {
    "enabled": false,
    "system": "SIMS",
    "apiEndpoint": ""
  }
}
```

---

## Low Priority Enhancements

### 9. Build MSI/Installer
**Purpose**: Non-technical college staff can install  
**Tool**: WiX Toolset or Advanced Installer  
**Features**:
- Install scripts to `Program Files\PersonalDevelopmentCoach\`
- Add to PATH
- Create desktop shortcuts
- Generate `college-config.json` template

### 10. Integrate with Personal Development Coach Agent
**Purpose**: Scripts + AI agent work together  
**Implementation**:
- Agent can call scripts via Task tool
- Shared memory: Agent reads script outputs
- Feedback loop: Agent analyzes reports, suggests improvements

### 11. Develop SaaS Web Dashboard
**Purpose**: College management portal  
**Features**:
- Cohort-wide analytics (attendance, targets, safeguarding)
- Staff dashboard (caseloads, alerts)
- Student portal (view targets, progress)
- Parent communication center

---

## File Inventory

| File | Status | Priority |
|------|--------|----------|
| `generate-report.ps1` | ⚠️ Needs fix #1, #2, #5, #6 | High |
| `attendance-monitor.ps1` | ⚠️ Needs fix #1, #2, #6 | High |
| `ucas-reference-generator.ps1` | ❌ Needs fix #1, #2, #3, #6 | High |
| `1-to-1-session-log.ps1` | ⚠️ Needs fix #2, #4, #6 | High |
| `set-targets.ps1` | ⚠️ Needs fix #2, #6 | Medium |
| `coaching-shortcuts.md` | ✅ Good | Low |
| `CoachingTools.psm1` | ❌ Create (fix #7) | Medium |
| `college-config.json` | ❌ Create (fix #8) | Medium |

---

## Next Session Instructions for Builder

```
/task builder
"Fix all critical bugs in the Personal Development Coach automation suite:

1. Strip ANSI codes from markdown outputs (keep for terminal only)
2. Replace hardcoded paths with relative paths
3. Fix UCAS script duplicate .md bug
4. Add automatic directory creation
5. Make generate-report.ps1 read real attendance.csv
6. Add error handling (try/catch) to all scripts
7. Create shared CoachingTools.psm1 module
8. Add college-config.json for multi-tenant support

Reference this file: 04_Active_Work/2026-04-28-todo/README.md
After fixing, update MEMORY.md and create session log."
```

---

## Revenue Impact

| Fix | Impact on Sales |
|------|----------------|
| ANSI in markdown | 🚨 Blocking (looks unprofessional) |
| Hardcoded paths | 🚨 Blocking (can't deploy to colleges) |
| UCAS bug | ⚠️ High (bad for pilot) |
| No error handling | ⚠️ Medium (breaks during demo) |
| Real CSV reading | ✅ Revenue enabler (real value) |
| Shared module | ✅ Maintainability |
| Multi-tenant | ✅ Scalability (sell to 100+ colleges) |

---

**Session End: 2026-04-28**  
**Next Builder Session**: Pick up from `04_Active_Work/2026-04-28-todo/README.md`  
**Goal**: Production-ready Personal Development Coach automation suite
