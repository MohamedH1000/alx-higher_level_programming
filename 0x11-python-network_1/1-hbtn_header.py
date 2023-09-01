#!/usr/bin/python3
"""
testing status of web pages by this script
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as moment:
        meta = moment.info()
        for first in meta._headers:
            if first[0] == 'X-Request-Id':
                print(first[1])
