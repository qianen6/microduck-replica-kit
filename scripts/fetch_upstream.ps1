param(
    [string]$Destination = (Join-Path $PSScriptRoot '..\upstream')
)

$ErrorActionPreference = 'Stop'
$lockPath = Join-Path $PSScriptRoot '..\source-lock.json'
$lock = Get-Content -LiteralPath $lockPath -Raw | ConvertFrom-Json

New-Item -ItemType Directory -Force -Path $Destination | Out-Null

foreach ($source in $lock.sources) {
    $folder = ($source.name -split '/')[-1]
    $target = Join-Path $Destination $folder
    if (Test-Path -LiteralPath $target) {
        throw "Target already exists: $target"
    }

    git init $target | Out-Null
    git -C $target remote add origin $source.url
    git -C $target fetch --depth 1 origin $source.commit
    git -C $target checkout --detach FETCH_HEAD | Out-Null

    $head = (git -C $target rev-parse HEAD).Trim()
    if ($head -ne $source.commit) {
        throw "Commit mismatch for $($source.name): expected $($source.commit), got $head"
    }
    Write-Output "SOURCE_LOCK PASS name=$($source.name) commit=$head path=$target"
}

