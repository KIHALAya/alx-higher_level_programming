#!/usr/bin/python3
""" 0-hbtn_status.py - Python script that
 fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    import sys

    args = sys.argv[1:]
    data = {"email": args[1]}
    encoded_data = urlencode(data).encode('utf-8')
    request = Request(args[0], data=encoded_data, method='POST')

    with urlopen(request) as response:
        content = response.read().decode('utf-8')
        print(content)
