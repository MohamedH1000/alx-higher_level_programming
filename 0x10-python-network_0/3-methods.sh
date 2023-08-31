#!/bin/bash
# get methods by this script
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
