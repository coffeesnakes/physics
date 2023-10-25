#!/bin/bash

# Get the location as a command line argument
location=$1

# Check the weather using wttr.in
curl "wttr.in/${location}"