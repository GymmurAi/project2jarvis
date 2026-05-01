param(
    [Parameter(Mandatory=$true)]
    [string]$StudentID,
    [Parameter(Mandatory=$true)]
    [string]$CaseloadCSV
)

# ANSI Color Codes
$ANSI_RESET = "`e[0m"
$ANSI_RED = "`e[31m"
$ANSI_GREEN = "`e[32m"
$ANSI_YELLOW = "`e[33m"
$ANSI_BLUE = "`e[34m"
$ANSI_BOLD = "`e[1m"
$ANSI_CYAN = "`e[36m"
$ANSI_MAGENTA = "`e[35m"

# Check if CSV exists
if (-not (Test-Path $CaseloadCSV)) {
    Write-Host "$ANSI_RED[ERROR] CSV file not found: $CaseloadCSV$ANSI_RESET"
    exit 1
}

# Read CSV
$students = Import-Csv $CaseloadCSV
$student = $students | Where-Object { $_.StudentID -eq $StudentID }

if (-not $student) {
    Write-Host "$ANSI_RED[ERROR] Student ID '$StudentID' not found in caseload$ANSI_RESET"
    exit 1
}

# Generate sample attendance data
$attendanceData = @(
    @{Date="2026-04-01"; Status="Present"},
    @{Date="2026-04-02"; Status="Present"},
    @{Date="2026-04-03"; Status="Late"},
    @{Date="2026-04-04"; Status="Present"},
    @{Date="2026-04-08"; Status="Present"},
    @{Date="2026-04-09"; Status="Absent"},
    @{Date="2026-04-10"; Status="Present"},
    @{Date="2026-04-11"; Status="Present"},
    @{Date="2026-04-15"; Status="Present"},
    @{Date="2026-04-16"; Status="Late"},
    @{Date="2026-04-17"; Status="Present"},
    @{Date="2026-04-18"; Status="Present"}
)

# Calculate attendance percentage
$totalSessions = $attendanceData.Count
$presentCount = ($attendanceData | Where-Object { $_.Status -eq "Present" }).Count
$lateCount = ($attendanceData | Where-Object { $_.Status -eq "Late" }).Count
$absentCount = ($attendanceData | Where-Object { $_.Status -eq "Absent" }).Count
$attendancePct = [math]::Round((($presentCount + ($lateCount * 0.5)) / $totalSessions) * 100, 1)

# Attendance Chart Function
function Generate-AttendanceChart {
    param($data)
    $chart = "`n$ANSI_BOLD$ANSI_BLUE[ATTENDANCE] Trend (Last 12 Sessions)$ANSI_RESET`n"
    $chart += "------------------------------------------------------------`n"
    foreach ($entry in $data) {
        $bar = "█" * (Get-Random -Minimum 1 -Maximum 4)
        $color = switch ($entry.Status) {
            "Present" { $ANSI_GREEN }
            "Late" { $ANSI_YELLOW }
            "Absent" { $ANSI_RED }
        }
        $chart += "$color$bar $($entry.Date): $($entry.Status)$ANSI_RESET`n"
    }
    $chart += "------------------------------------------------------------`n"
    return $chart
}

# Target completion data
$targets = @(
    @{Target="Complete Math coursework"; Status="Completed"; Deadline="2026-04-10"},
    @{Target="Attend 3 study skills sessions"; Status="In Progress"; Deadline="2026-05-01"},
    @{Target="Improve attendance to 90%"; Status="At Risk"; Deadline="2026-04-30"},
    @{Target="Submit English essay"; Status="Completed"; Deadline="2026-04-15"}
)

# Safeguarding flags
$safeguardingFlags = @()
if ($attendancePct -lt 85) { $safeguardingFlags += "[!] Low attendance ($attendancePct%)" }
if ($lateCount -gt 3) { $safeguardingFlags += "[!] Persistent lateness" }
if ($safeguardingFlags.Count -eq 0) { $safeguardingFlags += "[OK] No major concerns" }

# Generate report
$timestamp = Get-Date -Format "yyyy-MM-dd-HHmm"
$reportFile = "D:\Projects\Project2Jarvis\04_Active_Work\$StudentID-report-$timestamp.md"

$attendanceColor = if ($attendancePct -ge 95) { $ANSI_GREEN } elseif ($attendancePct -ge 85) { $ANSI_YELLOW } else { $ANSI_RED }

$reportContent = @"
# Student Progress Report
*Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm")*

## Student Information
- **Name**: $($student.Name)
- **Student ID**: $StudentID
- **Tutor Group**: $($student.TutorGroup)
- **Year**: $($student.Year)

## Attendance Summary
- **Overall Attendance**: $ANSI_BOLD$attendanceColor$attendancePct%$ANSI_RESET
- **Present**: $presentCount sessions
- **Late**: $lateCount sessions
- **Absent**: $absentCount sessions

$(Generate-AttendanceChart -data $attendanceData)

## Target Completion Status
$ANSI_BOLD$ANSI_BLUE------------------------------------------------------------$ANSI_RESET
$(foreach ($t in $targets) {
    $statusColor = switch ($t.Status) {
        "Completed" { $ANSI_GREEN }
        "In Progress" { $ANSI_YELLOW }
        "At Risk" { $ANSI_RED }
        default { $ANSI_RESET }
    }
    "$statusColor[$(switch ($t.Status) { "Completed" { "OK" }; "In Progress" { ">>" }; "At Risk" { "!!" } })] $($t.Target) - $($t.Status) (Deadline: $($t.Deadline))$ANSI_RESET"
})
$ANSI_BOLD$ANSI_BLUE------------------------------------------------------------$ANSI_RESET

## Safeguarding Flags
$(foreach ($flag in $safeguardingFlags) { "- $flag" })

## Next Steps & Recommendations
1. **Attendance**: $(if ($attendancePct -lt 85) { "[URGENT] Meeting required to discuss attendance concerns" } else { "[OK] Attendance is satisfactory" })
2. **Targets**: Review progress on "$($targets[1].Target)" - deadline approaching
3. **Support**: $(if ($lateCount -gt 2) { "Consider time management workshop" } else { "No additional support needed at this time" })
4. **Follow-up**: Schedule next review for $(Get-Date (Get-Date).AddDays(21) -Format "yyyy-MM-dd")

## Action Items
- [ ] Send attendance report to parents/guardians
- [ ] Book intervention meeting if attendance <85%
- [ ] Update target tracker
- [ ] Log safeguarding concerns in main system

---
*Report generated by Project2Jarvis Coaching Automation*
"@

# Save report
$reportContent | Out-File -FilePath $reportFile -Encoding utf8

# Display summary
Write-Host "`n$ANSI_BOLD$ANSI_MAGENTA========================================$ANSI_RESET"
Write-Host "$ANSI_CYAN[STUDENT REPORT GENERATED]$ANSI_RESET"
Write-Host "$ANSI_BOLD$ANSI_MAGENTA========================================$ANSI_RESET"
Write-Host "$ANSI_GREEN[OK] Report saved to:$ANSI_RESET"
Write-Host "$ANSI_YELLOW$reportFile$ANSI_RESET"
Write-Host "`n$ANSI_BOLD[SUMMARY]$ANSI_RESET"
Write-Host "  Student: $($student.Name) ($StudentID)"
Write-Host "  Attendance: $attendancePct%"
Write-Host "  Safeguarding Flags: $($safeguardingFlags.Count)"
Write-Host "$ANSI_BOLD$ANSI_MAGENTA========================================$ANSI_RESET`n"
