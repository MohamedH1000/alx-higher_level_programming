#!/usr/bin/python3
"""
testing status of web pages by this script
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as moment:
            print(moment.read().decode('utf-8'))
    except urllib.error.HTTPError as a:
        print("Error code: {}".format(a.code))
