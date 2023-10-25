# Get the location as a command line argument
param (
    [Parameter(Mandatory=$true)]
    [string]$location
)

# Check the weather using wttr.in
$response = Invoke-WebRequest -Uri "http://wttr.in/$location"

# Print the weather information
$response.Content#!/bin/bash

# Get the location as a command line argument
location=$1

# Check the weather using wttr.in
curl "wttr.in/${location}"

# chmod +x getWeather.sh // icacls .\getWeather.sh /grant Everyone:F

