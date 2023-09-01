#!/usr/bin/python3
"""
status of web pages to be tested by this script
"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    moment = requests.get(url)
    prirz = moment.headers
    print(prirz.get('X-Request-Id'))
