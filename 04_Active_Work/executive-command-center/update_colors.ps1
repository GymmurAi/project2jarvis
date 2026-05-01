# Update HTML to use high-grade navy/teal palette
$content = Get-Content "D:\Projects\Project2Jarvis\04_Active_Work\executive-command-center\index.html" -Raw

# Replace gold with navy (authority) for most elements
$content = $content -replace "stroke=`"var(--gold-500)`"", "stroke=`"var(--navy-500)`""
$content = $content -replace "fill=`"var(--gold-500)`"", "fill=`"var(--navy-500)`""

# Replace violet with teal (data visualization)
$content = $content -replace "stroke=`"var(--violet-500)`"", "stroke=`"var(--teal-500)`""
$content = $content -replace "fill=`"var(--violet-500)`"", "fill=`"var(--teal-500)`""

# Keep gold ONLY for revenue KPIs (signal)
# (lines 160, 163 - Revenue Potential)

# Replace text colors
$content = $content -replace "var(--text-secondary)`"", "var(--navy-400)`""
$content = $content -replace "var(--text-muted)`"", "var(--navy-500)`""

$content | Set-Content "D:\Projects\Project2Jarvis\04_Active_Work\executive-command-center\index_updated.html" -Force
Write-Host "Updated HTML with high-grade palette"