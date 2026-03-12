$csvPath = "/workspaces/DE_Practice/sample.csv"
$userData = Import-Csv -Path $csvPath -Delimiter "`t"

$userData.error


foreach($er in $userData.error){
    $username = ($line -match "Processing mailbox:\s*(.*?)\s*completed")[1]
    $officeID = ($line -match "(ID:\s*([0-9a-zA-Z-]+))")[1]

    Write-Host "$($username) has $($officeID)"
}

$string = "[Warning] Processing mailbox: Reena Rollason completed with warning: User was not found: Reena Rollason (ID: 101970cc-7acd-4a30-a1b8-0a84293197c5)."

$username = $string -match "Processing mailbox:\s*(?<username>.*?)\s*completed"
$Matches['username']
$officeId = $string -match "\(ID:\s*(?<officeId>[0-9a-zA-Z-]+)\)"
$Matches['officeId']

$eregex = $string -match "Processing mailbox:\s*(?<username>.*?)\s*\(ID:\s*(?<officeId>[0-9a-zA-Z-]+)\)"
$Matches['officeId']
$Matches['username']

