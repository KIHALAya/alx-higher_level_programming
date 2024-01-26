#!/usr/bin/python3
""" 0-hbtn_status.py - Python script that
 fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib.request import urlopen
    import sys

    args = sys.argv[1:]
    with urlopen(args[0]) as response:
        headers = response.info()
        X_R_ID = headers.get("X-Request-Id")
        print(X_R_ID)
