#!/bin/bash
# the body size of a request to be get by this script
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
