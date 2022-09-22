#!/bin/bash
# Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

response=$(curl -s -o /dev/null -I -w "%{http_code}" codekami.tech)

if [[ "$response" -eq 200 ]]; then
    # curl -s -o /dev/null -I -w "%{size_download}" "$1"
    curl -s -L -I "$1" | awk -v IGNORECASE=1 '/^Content-Length/ { print $2 }'
fi
