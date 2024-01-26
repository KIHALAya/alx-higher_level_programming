#!/usr/bin/python3

""" 0-hbtn_status.py - Python script that
fetches https://alx-intranet.hbtn.io/status"""

from urllib.request import urlopen
url = "https://alx-intranet.hbtn.io/status"
response = urlopen(url)
content = response.read()
print(
    """Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(
        type(content), content, content.decode('utf-8'))
)
