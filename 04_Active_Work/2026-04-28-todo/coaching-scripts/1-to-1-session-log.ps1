param(
    [Parameter(Mandatory=$true)]
    [string]$StudentName,
    [Parameter(Mandatory=$true)]
    [ValidateSet("1:1", "Group")]
    [string]$SessionType,
    [Parameter(Mandatory=$false)]
    [string]$Notes = ""
)

# ANSI Color Codes
$ANSI_RESET = "`e[0m"
$ANSI_RED = "`e[31m"
$ANSI_GREEN = "`e[32m"
$ANSI_YELLOW = "`e[33m"
$ANSI_BLUE = "`e[34m"
$ANSI_BOLD = "`e[1m"
$ANSI_CYAN = "`e[36m"

$timestamp = Get-Date -Format "yyyy-MM-dd"
$sessionFile = "D:\Projects\Project2Jarvis\04_Active_Work\sessions\$StudentName-$timestamp.md"

# Get GROW model inputs
Write-Host "$ANSI_BOLD$ANSI_BLUE[1] GROW Model Sections$ANSI_RESET"
$goal = Read-Host "Goal (What does the student want to achieve?)"
$reality = Read-Host "Reality (What is current situation?)"
$options = Read-Host "Options (What alternatives exist?)"
$will = Read-Host "Will (What will they commit to?)"

# SMART target setter
Write-Host "`n$ANSI_BOLD$ANSI_YELLOW[2] SMART Target Setter$ANSI_RESET"
$smartSpecific = Read-Host "Specific (What exactly?)"
$smartMeasurable = Read-Host "Measurable (How to track?)"
$smartAchievable = Read-Host "Achievable (Is it realistic?)"
$smartRelevant = Read-Host "Relevant (Why this target?)"
$smartTimeBound = Read-Host "Time-bound (Deadline?)"

# Safeguarding checklist
Write-Host "`n$ANSI_BOLD$ANSI_RED[3] Safeguarding Checklist$ANSI_RESET"
$sg1 = Read-Host "Any immediate risk? (Y/N)"
$sg2 = Read-Host "Mental health concerns? (Y/N)"
$sg3 = Read-Host "Bullying/harassment? (Y/N)"
$sgNotes = Read-Host "Safeguarding notes (optional)"

# Follow-up actions
Write-Host "`n$ANSI_BOLD$ANSI_GREEN[4] Follow-up Actions$ANSI_RESET"
$followUp1 = Read-Host "Action 1"
$followUp2 = Read-Host "Action 2 (optional)"
$followUp3 = Read-Host "Action 3 (optional)"

# Generate session log content
$content = @"
# 1:1 Session Log - $StudentName
*Date: $timestamp*
*Session Type: $SessionType*

## [GROW] GROW Model
### Goal
$goal

### Reality
$reality

### Options
$options

### Will
$will

## [TARGET] SMART Target
- **Specific**: $smartSpecific
- **Measurable**: $smartMeasurable
- **Achievable**: $smartAchievable
- **Relevant**: $smartRelevant
- **Time-bound**: $smartTimeBound

## [!] Safeguarding Checklist
- Immediate risk: $sg1
- Mental health concerns: $sg2
- Bullying/harassment: $sg3
- Notes: $sgNotes

## [ACTION] Follow-up Actions
1. $followUp1
$(if ($followUp2) { "2. $followUp2" })
$(if ($followUp3) { "3. $followUp3" })

## [>>] Next Steps
1. Send session summary to student within 24 hours
2. Update target tracker with new SMART target
3. Schedule next session for $(Get-Date (Get-Date).AddDays(14) -Format "yyyy-MM-dd")
4. Log follow-up actions in student tracker
"@

# Save session log
$content | Out-File -FilePath $sessionFile -Encoding utf8

# Display confirmation
Write-Host "`n$ANSI_BOLD$ANSI_CYAN========================================$ANSI_RESET"
Write-Host "$ANSI_GREEN[OK] Session log saved to:$ANSI_RESET"
Write-Host "$ANSI_YELLOW$sessionFile$ANSI_RESET"
Write-Host "$ANSI_BOLD$ANSI_CYAN========================================$ANSI_RESET`n"
