# 🚀 Coaching Automation Quick Reference

*Quick reference for all Personal Development Coach automation scripts*

## 📋 Available Scripts

### 1. `generate-report.ps1` - Student Progress Reports
Automatically generates comprehensive student progress reports with attendance trends, target completion, and safeguarding flags.

**Usage:**
```powershell
cd 04_Active_Work/coaching-scripts
./generate-report.ps1 -StudentID "ST001" -CaseloadCSV "caseload.csv"
```

**What it does:**
- Reads student data from CSV
- Calculates attendance trends with ASCII charts
- Shows target completion status
- Flags safeguarding concerns
- Generates formatted markdown report

**Next Steps:** Review report, share with student, log concerns

---

### 2. `1-to-1-session-log.ps1` - Session Logging
Creates detailed 1:1 or group session logs with GROW model, SMART targets, and safeguarding checklist.

**Usage:**
```powershell
cd 04_Active_Work/coaching-scripts
./1-to-1-session-log.ps1 -StudentName "John Doe" -SessionType "1:1"
```

**What it does:**
- Interactive GROW model input (Goal, Reality, Options, Will)
- SMART target setter
- Safeguarding checklist
- Auto-saves to `04_Active_Work/sessions/`

**Next Steps:** Send summary to student within 24h, update tracker

---

### 3. `set-targets.ps1` - SMART Target Setting
Interactive tool for creating SMART targets with progress tracking charts.

**Usage:**
```powershell
cd 04_Active_Work/coaching-scripts
./set-targets.ps1
```

**What it does:**
- Guides through SMART framework (Specific, Measurable, Achievable, Relevant, Time-bound)
- Creates progress tracking chart
- Sets review dates automatically
- Saves to student target file

**Next Steps:** Share with student, set weekly check-ins, update tracker

---

### 4. `attendance-monitor.ps1` - Attendance Monitoring
Checks attendance CSV and flags students with concerns (<85% warning, <75% critical).

**Usage:**
```powershell
cd 04_Active_Work/coaching-scripts
./attendance-monitor.ps1 -AttendanceCSV "attendance.csv"
```

**What it does:**
- Calculates attendance % for all students
- Flags concerns with emojis (🚨 Critical, ⚠️ Warning, ✅ Good)
- Generates ASCII attendance charts
- Creates alerts file with next steps

**Next Steps:** Contact parents, send letters, schedule meetings

---

### 5. `ucas-reference-generator.ps1` - UCAS References
Creates UCAS references (max 4000 chars) with academic performance, personal qualities, and recommendation.

**Usage:**
```powershell
cd 04_Active_Work/coaching-scripts
./ucas-reference-generator.ps1
```

**What it does:**
- Interactive input for student achievements
- Generates 4000-char reference
- Sections: Academic, Personal, Extracurricular, Recommendation
- Saves to `04_Active_Work/ucas-refs/`

**Next Steps:** Review with student, sign, submit to UCAS

---

## 🎯 Sample Commands

### Generate a student report:
```powershell
./generate-report.ps1 -StudentID "ST001" -CaseloadCSV "caseload.csv"
```

### Log a 1:1 session:
```powershell
./1-to-1-session-log.ps1 -StudentName "Jane Smith" -SessionType "1:1"
```

### Set SMART targets:
```powershell
./set-targets.ps1
# Then follow interactive prompts
```

### Monitor attendance:
```powershell
./attendance-monitor.ps1 -AttendanceCSV "attendance.csv"
```

### Generate UCAS reference:
```powershell
./ucas-reference-generator.ps1
# Then follow interactive prompts
```

---

## 📁 Output Locations

| Script | Output Location |
|--------|----------------|
| `generate-report.ps1` | `04_Active_Work/{StudentID}-report-YYYY-MM-DD-HHMM.md` |
| `1-to-1-session-log.ps1` | `04_Active_Work/sessions/{StudentName}-YYYY-MM-DD.md` |
| `set-targets.ps1` | `04_Active_Work/{StudentID}-targets.md` |
| `attendance-monitor.ps1` | `04_Active_Work/attendance-alerts-YYYY-MM-DD.md` |
| `ucas-reference-generator.ps1` | `04_Active_Work/ucas-refs/{StudentName}-ucas-ref-YYYY-MM-DD.md` |

---

## ⚡ Time Saved

| Task | Manual Time | Automated Time | Time Saved |
|------|-------------|----------------|------------|
| Student Report | 45 mins | 5 mins | 40 mins |
| Session Log | 20 mins | 3 mins | 17 mins |
| Target Setting | 30 mins | 5 mins | 25 mins |
| Attendance Review | 60 mins | 5 mins | 55 mins |
| UCAS Reference | 90 mins | 10 mins | 80 mins |
| **TOTAL per week** | **245 mins** | **28 mins** | **217 mins (88%)** |

---

## 🎯 Next Steps After Running Any Script

1. **Review** the generated output file
2. **Share** with relevant parties (student, parents, staff)
3. **Log** any concerns in main systems
4. **Schedule** follow-up actions
5. **Update** tracking spreadsheets/databases

---

*Scripts located in: `04_Active_Work/coaching-scripts/`*
*Part of Project2Jarvis Personal Development Coach automation*
