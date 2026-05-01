param()

# ANSI Color Codes
$ANSI_RESET = "`e[0m"
$ANSI_RED = "`e[31m"
$ANSI_GREEN = "`e[32m"
$ANSI_YELLOW = "`e[33m"
$ANSI_BLUE = "`e[34m"
$ANSI_BOLD = "`e[1m"
$ANSI_CYAN = "`e[36m"
$ANSI_MAGENTA = "`e[35m"

Write-Host "`n$ANSI_BOLD$ANSI_CYAN========================================$ANSI_RESET"
Write-Host "$ANSI_YELLOW[SMART] SMART TARGET SETTER$ANSI_RESET"
Write-Host "$ANSI_BOLD$ANSI_CYAN========================================$ANSI_RESET`n"

# Get student details
Write-Host "$ANSI_BOLD$ANSI_BLUE[1] Student Information$ANSI_RESET"
$studentName = Read-Host "Student Name"
$studentID = Read-Host "Student ID"
$subject = Read-Host "Subject/Area"

# SMART target creation
Write-Host "`n$ANSI_BOLD$ANSI_YELLOW[2] SMART Target Guide$ANSI_RESET"
Write-Host "$ANSI_CYAN------------------------------------------------------------$ANSI_RESET"

Write-Host "`n$ANSI_BOLD$ANSI_GREEN[S]pecific$ANSI_RESET - What exactly do you want to achieve?"
$specific = Read-Host "  > "

Write-Host "`n$ANSI_BOLD$ANSI_GREEN[M]easurable$ANSI_RESET - How will you track progress?"
$measurable = Read-Host "  > "

Write-Host "`n$ANSI_BOLD$ANSI_GREEN[A]chievable$ANSI_RESET - Is this realistic for the student?"
$achievable = Read-Host "  > "

Write-Host "`n$ANSI_BOLD$ANSI_GREEN[R]elevant$ANSI_RESET - Why is this target important?"
$relevant = Read-Host "  > "

Write-Host "`n$ANSI_BOLD$ANSI_GREEN[T]ime-bound$ANSI_RESET - What is the deadline?"
$deadline = Read-Host "  > "

# Additional tracking
Write-Host "`n$ANSI_BOLD$ANSI_BLUE[3] Progress Tracking$ANSI_RESET"
$milestone1 = Read-Host "Milestone 1 (optional)"
$milestone2 = Read-Host "Milestone 2 (optional)"
$successCriteria = Read-Host "Success criteria"

# Progress tracking chart (ASCII)
function Generate-ProgressChart {
    param($deadlineDate)
    $today = Get-Date
    $endDate = Get-Date $deadlineDate
    $totalDays = ($endDate - $today).Days
    $elapsedDays = 0
    $progressPct = 0

    $chart = "`n$ANSI_BOLD$ANSI_CYAN[CHART] Progress Tracking Chart$ANSI_RESET`n"
    $chart += "$ANSI_YELLOW------------------------------------------------------------$ANSI_RESET`n"
    $chart += "Target Period: $today to $endDate ($totalDays days)`n`n"

    # Create visual bar
    $barLength = 40
    $filledBars = [math]::Round(($elapsedDays / $totalDays) * $barLength)
    $bar = ""
    for ($i = 0; $i -lt $barLength; $i++) {
        if ($i -lt $filledBars) { $bar += "█" }
        else { $bar += "░" }
    }
    $chart += "$ANSI_GREEN$bar$ANSI_RESET $progressPct%`n"
    $chart += "$ANSI_YELLOW------------------------------------------------------------$ANSI_RESET`n"
    return $chart
}

# Save target to file
$timestamp = Get-Date -Format "yyyy-MM-dd"
$targetFile = "D:\Projects\Project2Jarvis\04_Active_Work\$studentID-targets.md"

$targetContent = @"
# [TARGET] SMART Target - $studentName
*Created: $timestamp*
*Student ID: $studentID*
*Subject: $subject*

## SMART Framework
| Element | Details |
|---------|---------|
| **Specific** | $specific |
| **Measurable** | $measurable |
| **Achievable** | $achievable |
| **Relevant** | $relevant |
| **Time-bound** | $deadline |

## [CHART] Progress Tracking
$(Generate-ProgressChart -deadlineDate $deadline)

### Milestones
$(if ($milestone1) { "1. $milestone1" })
$(if ($milestone2) { "2. $milestone2" })

### Success Criteria
$successCriteria

## [CALENDAR] Review Dates
- **Created**: $timestamp
- **First Review**: $(Get-Date (Get-Date).AddDays(7) -Format "yyyy-MM-dd")
- **Mid-point Review**: $(Get-Date (Get-Date $deadline).AddDays(-7) -Format "yyyy-MM-dd")
- **Final Review**: $deadline

## [>>] Next Steps
1. Share target with student and get their commitment
2. Set up weekly check-ins to monitor progress
3. Update progress tracking chart after each session
4. Celebrate milestone achievements
5. Document evidence of progress for portfolio

---
*Target set by Project2Jarvis Coaching Automation*
"@

# Save to file
$targetContent | Out-File -FilePath $targetFile -Encoding utf8

# Display confirmation
Write-Host "`n$ANSI_BOLD$ANSI_MAGENTA========================================$ANSI_RESET"
Write-Host "$ANSI_GREEN[OK] SMART Target Saved!$ANSI_RESET"
Write-Host "$ANSI_BOLD$ANSI_MAGENTA========================================$ANSI_RESET"
Write-Host "$ANSI_CYAN File: $targetFile$ANSI_RESET"
Write-Host "`n$ANSI_BOLD[SUMMARY]$ANSI_RESET"
Write-Host "  Student: $studentName ($studentID)"
Write-Host "  Subject: $subject"
Write-Host "  Deadline: $deadline"
Write-Host "$ANSI_BOLD$ANSI_MAGENTA========================================$ANSI_RESET`n"
