#!/bin/bash
# Print options in HEAD & made by MEGA
curl -sI "$1" | grep "Allow:" | cut -d" " -f2-
