$files = Get-ChildItem -Path "chapters" -Filter "*.html"

foreach ($file in $files) {
    $raw = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)

    # Fix \rightarrow split by carriage return or form feed
    $raw = $raw -replace "[\r\n]*ightarrow", " \rightarrow "
    
    # Fix \frac (Form Feed + rac -> \frac)
    $raw = $raw -replace "\x0crac", "\frac"
    $raw = $raw -replace "rac", "\frac"

    # Fix \text (Tab + ext -> \text)
    $raw = $raw -replace "\x09ext", "\text"
    $raw = $raw -replace "	ext", "\text"

    # Fix \times (Tab + imes -> \times)
    $raw = $raw -replace "\x09imes", "\times"
    $raw = $raw -replace "	imes", "\times"

    # Fix \theta (Tab + heta -> \theta)
    $raw = $raw -replace "\x09heta", "\theta"
    $raw = $raw -replace "	heta", "\theta"

    # Fix \Rightarrow (\R \rightarrow -> \Rightarrow)
    $raw = $raw -replace "\\R\s*\\rightarrow", "\Rightarrow"
    $raw = $raw -replace "R\s*\\rightarrow", "\Rightarrow"

    [System.IO.File]::WriteAllText($file.FullName, $raw, [System.Text.Encoding]::UTF8)
    Write-Host "Cleaned LaTeX escapes in: $($file.Name)"
}
