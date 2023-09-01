#!/bin/bash
# testing a server and posting a json data file by this bash script
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
