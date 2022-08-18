#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -siLX "OPTIONS" "$1" | grep -i "ALLOW" | cut -d " " -f2-
