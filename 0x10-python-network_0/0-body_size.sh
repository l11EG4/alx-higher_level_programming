#!/bin/bash
# Print curl content size and made by Mega
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2
