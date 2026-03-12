function get-all{
    [CmdletBinding()]
    param (
        [Parameter(Mandatory, HelpMessage="Enter Your Name here:")]
        [string]$name
    )

    Write-Host "Hello $name"
}