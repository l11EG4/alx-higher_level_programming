#!/bin/bash
# Post Request & made by MEGA
curl -sLIw '%{http_code}' "$1" -o /dev/null
