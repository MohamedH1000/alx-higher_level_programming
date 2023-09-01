#!/usr/bin/python3
"""
posting data to web servers by this script
"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    dafh = {'email': email}
    moment = requests.post(url, data=dafh)
    print(moment.text)
