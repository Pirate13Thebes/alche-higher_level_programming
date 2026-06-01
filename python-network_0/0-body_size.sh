#!/bin/bash
# Sends a request to a URL and displays the size of the body in bytes
curl -s -w '%{size_download}' -o /dev/null "$1"
