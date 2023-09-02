#!/usr/bin/python3
"""posting data to star war api by this script
"""
if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys
    url = "https://api.github.com/"
    user_url = url + "user"
    username = sys.argv[1]
    password = sys.argv[2]
    moment = requests.get(user_url,
                            auth=HTTPBasicAuth(username,
                                               password))
    if moment.status_code == requests.codes.ok and len(moment.text) > 0:
        try:
            object_mine = moment.json()
            print(object_mine.get('id'))
        except ValueError as invalid_json:
            print('Not a valid JSON')
    else:
        print(None)
