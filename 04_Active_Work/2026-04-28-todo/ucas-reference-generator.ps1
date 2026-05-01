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
Write-Host "$ANSI_YELLOW[GRAD] UCAS REFERENCE GENERATOR$ANSI_RESET"
Write-Host "$ANSI_BOLD$ANSI_CYAN========================================$ANSI_RESET`n"

# Get student information
Write-Host "$ANSI_BOLD$ANSI_BLUE[1] Student Information$ANSI_RESET"
$studentName = Read-Host "Student Name"
$studentID = Read-Host "Student ID"

Write-Host "`n$ANSI_BOLD$ANSI_BLUE[2] Academic Performance$ANSI_RESET"
$qualification = Read-Host "Qualification (e.g., BTEC, A-Level)"
$subject1 = Read-Host "Subject 1 & Predicted Grade"
$subject2 = Read-Host "Subject 2 & Predicted Grade"
$subject3 = Read-Host "Subject 3 & Predicted Grade (optional)"
$academicComment = Read-Host "Academic strengths/comments"

Write-Host "`n$ANSI_BOLD$ANSI_GREEN[3] Personal Qualities$ANSI_RESET"
$personalQualities = Read-Host "Key personal qualities (comma-separated)"
$extracurricular = Read-Host "Extracurricular activities"
$workExperience = Read-Host "Work experience/placements"

Write-Host "`n$ANSI_BOLD$ANSI_YELLOW[4] Course & Career$ANSI_RESET"
$chosenCourse = Read-Host "Chosen course/university"
$careerAspirations = Read-Host "Career aspirations"
$whySuitable = Read-Host "Why suitable for this course"

# Generate reference (max 4000 chars)
$timestamp = Get-Date -Format "yyyy-MM-dd"
$refFile = "D:\Projects\Project2Jarvis\04_Active_Work\ucas-refs\$studentName-ucas-ref-$timestamp.md"

function Generate-Reference {
    param(
        $Name, $ID, $Qual, $S1, $S2, $S3,
        $AcadComment, $Qualities, $Extra, $WorkExp,
        $Course, $Career, $Suitable
    )

    $ref = "UCAS REFERENCE`n"
    $ref += "=============`n`n"
    $ref += "Student: $Name ($ID)`n"
    $ref += "Date: $(Get-Date -Format 'dd MMMM yyyy')`n`n"

    $ref += "ACADEMIC PERFORMANCE`n"
    $ref += "--------------------`n"
    $ref += "Currently studying: $Qual`n"
    $ref += "Predicted Grades:`n"
    $ref += "- $S1`n"
    $ref += "- $S2`n"
    if ($S3) { $ref += "- $S3`n" }
    $ref += "`n$AcadComment`n`n"

    $ref += "PERSONAL QUALITIES`n"
    $ref += "-----------------`n"
    $ref += "$Qualities`n`n"

    $ref += "EXTRACURRICULAR ACTIVITIES`n"
    $ref += "--------------------------`n"
    $ref += "$Extra`n`n"

    if ($WorkExp) {
        $ref += "WORK EXPERIENCE`n"
        $ref += "--------------`n"
        $ref += "$WorkExp`n`n"
    }

    $ref += "COURSE SUITABILITY`n"
    $ref += "------------------`n"
    $ref += "Chosen Course: $Course`n"
    $ref += "Career Aspirations: $Career`n`n"
    $ref += "$Suitable`n`n"

    $ref += "RECOMMENDATION`n"
    $ref += "--------------`n"
    $ref += "I am pleased to recommend $Name for $Course. "
    $ref += "$Name has demonstrated consistent commitment to studies and shows great potential "
    $ref += "in their chosen field. Their combination of academic ability and personal qualities "
    $ref += "make them an excellent candidate for this course.`n`n"
    $ref += "I have no hesitation in recommending $Name and believe they will be an asset to your institution.`n`n"
    $ref += "Yours sincerely,`n`n"
    $ref += "[Tutor Name]`n"
    $ref += "[Tutor Title]`n"
    $ref += "[Institution]`n"

    # Check character count
    if ($ref.Length -gt 4000) {
        Write-Host "$ANSI_YELLOW[WARN] Reference exceeds 4000 characters ($($ref.Length)). Trimming...$ANSI_RESET"
        $ref = $ref.Substring(0, 3997) + "..."
    }

    return $ref
}

$reference = Generate-Reference -Name $studentName -ID $studentID -Qual $qualification `
    -S1 $subject1 -S2 $subject2 -S3 $subject3 -AcadComment $academicComment `
    -Qualities $personalQualities -Extra $extracurricular -WorkExp $workExperience `
    -Course $chosenCourse -Career $careerAspirations -Suitable $whySuitable

# Save reference
$reference | Out-File -FilePath $refFile -Encoding utf8

# Create markdown version with next steps
$mdContent = @"
# [GRAD] UCAS Reference - $studentName
*Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm")*

## [DOC] Reference Document
\`\`\`
$reference
\`\`\`

## [STATS] Reference Stats
- **Character Count**: $($reference.Length) / 4000
- **Word Count**: $(($reference -split '\s+').Count)
- **Student**: $studentName
- **Course**: $chosenCourse

## [>>] Next Steps for Student
1. **Review**: Read through the reference carefully
2. **Feedback**: Discuss any changes needed with tutor
3. **Application**: Add reference to UCAS application
4. **Deadline**: Ensure application submitted by UCAS deadline
5. **Backup**: Save copy of reference for personal records

## [>>] Next Steps for Tutor
1. **Sign**: Add digital/physical signature to final version
2. **Submit**: Upload to UCAS system or send to school/college
3. **Copy**: Keep copy in student file
4. **Follow-up**: Check student has submitted application
5. **Support**: Offer help with personal statement if needed

## [CHECK] Checklist
- [ ] Reference reviewed by student
- [ ] Any corrections made
- [ ] Tutor signature added
- [ ] Submitted to UCAS
- [ ] Copy filed in student records

---
*Reference generated by Project2Jarvis UCAS Automation*
*Character Count: $($reference.Length) / 4000*
"@

# Save markdown version
$mdContent | Out-File -FilePath "$refFile.md" -Encoding utf8 -Append

# Display summary
Write-Host "`n$ANSI_BOLD$ANSI_MAGENTA========================================$ANSI_RESET"
Write-Host "$ANSI_GREEN[OK] UCAS REFERENCE GENERATED!$ANSI_RESET"
Write-Host "$ANSI_BOLD$ANSI_MAGENTA========================================$ANSI_RESET"
Write-Host "$ANSI_CYAN File: $refFile$ANSI_RESET"
Write-Host "`n$ANSI_BOLD[STATS]$ANSI_RESET"
Write-Host "  Student: $studentName"
Write-Host "  Course: $chosenCourse"
Write-Host "  Character Count: $($reference.Length) / 4000"
Write-Host "$ANSI_BOLD$ANSI_MAGENTA========================================$ANSI_RESET`n"
