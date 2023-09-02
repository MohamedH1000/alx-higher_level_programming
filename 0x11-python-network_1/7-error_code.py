#!/usr/bin/python3
"""
posting data to web servers by this script
"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    moment = requests.get(url)
    if moment.status_code != requests.codes.ok:
        print('Error code: {}'.format(moment.status_code))
    else:
        print(moment.text)
