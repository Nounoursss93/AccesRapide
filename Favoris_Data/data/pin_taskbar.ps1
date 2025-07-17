param (
    [string]$filePath
)

$shell = New-Object -ComObject Shell.Application
$folder = $shell.Namespace((Split-Path $filePath))
$item = $folder.ParseName((Split-Path $filePath -Leaf))

$verbs = $item.Verbs()
foreach ($verb in $verbs) {
    if ($verb.Name.replace('&','') -match 'Épingler à la barre des tâches') {
        $verb.DoIt()
        Write-Host "Épinglé avec succès : $filePath"
        break
    }
}
