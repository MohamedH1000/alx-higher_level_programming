#!/usr/bin/python3
"""
positioning date to web servers by this script
"""
if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    tables = {'q': q}
    moment = requests.post(url, data=tables)
    if moment.status_code != requests.codes.ok or len(moment.text) <= 0:
        print('No result')
        sys.exit()
    else:
        try:
            object_mine = moment.json()
            if len(object_mine) == 0:
                print('No result')
                sys.exit()
            my_id = object_mine.get('id')
            my_name = object_mine.get('name')
            print("[{}] {}".format(my_id, my_name))
        except ValueError as invalid_json:
            print('Not a valid JSON')
