#!/usr/bin/python3
""" 0-hbtn_status.py - Python script that
 fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib.request import urlopen
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        content = response.read()
        print(
            """Body response:
            - type: {}
            - content: {}
            - utf8 content: {}""".format(
                type(content), content, content.decode('utf-8'))
        )
