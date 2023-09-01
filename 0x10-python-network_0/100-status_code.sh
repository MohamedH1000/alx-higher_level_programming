#!/bin/bash
# state code of a server to be displayed by this bash script
curl -L -s -X HEAD -w "%{http_code}" "$1"
