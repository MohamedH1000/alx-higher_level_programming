#!/usr/bin/python3
"""
test requesting post to server by this script
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    amouofpay = {'email': email}
    amouofpay = urllib.parse.urlencode(amouofpay)
    amouofpay = amouofpay.encode('ascii')
    req = urllib.request.Request(url, amouofpay)
    with urllib.request.urlopen(req) as moment:
        print(moment.read().decode('utf-8'))
