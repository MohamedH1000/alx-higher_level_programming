#!/usr/bin/python3
"""
tests status of web pages by this script
"""
if __name__ == "__main__":
    import urllib.request
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        bytes_content = response.read()
        content = bytes_content.decode('utf-8')
        str_to_be_printed = '''Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}'''.format(type(bytes_content), bytes_content, content)
        print(str_to_be_printed)
