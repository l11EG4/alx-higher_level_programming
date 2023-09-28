#!/bin/bash
# Made by MEGA
# Print curl content size
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2
