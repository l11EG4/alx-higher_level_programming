#!/bin/bash
# Post Request & made by MEGA
curl -sLX POST -H 'Content-Type: application/json' -d @"$2" "$1"
