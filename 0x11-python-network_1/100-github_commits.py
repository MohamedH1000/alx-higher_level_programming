#!/usr/bin/python3
"""
posting data to star war api by this script
"""
if __name__ == "__main__":
    import requests
    import sys
    url = "https://api.github.com/"
    username = sys.argv[1]
    repo = sys.argv[2]
    commits_url = url + "repos/{}/{}/commits".format(username, repo)
    moment = requests.get(commits_url)
    if moment.status_code == requests.codes.ok and len(moment.text) > 0:
        try:
            object_mine = moment.json()
            for a, b in enumerate(object_mine):
                if a == 10:
                    break
                if type(object_mine) is dict:
                    name = b.get('commit').get('author').get('name')
                    print("{}: {}".format(b.get('sha'), name))
        except ValueError as invalid_json:
            pass
