#!/usr/bin/python3
"""
status of web pagves to be tested by this script
"""
if __name__ == "__main__":
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    moment = requests.get(url)
    mohtawa = moment.text
    print_str = '''Body response:
\t- type: {}
\t- content: {}'''.format(type(mohtawa), mohtawa)
    print(print_str)
