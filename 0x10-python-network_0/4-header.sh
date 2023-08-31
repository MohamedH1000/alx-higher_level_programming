#!/bin/bash
# custom headers to be send to servers by this script
curl -s -H "X-School-User-Id: 98" "$1"
