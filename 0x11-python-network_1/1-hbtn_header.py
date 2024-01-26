#!/usr/bin/python3
""" 1-hbtn_header.py -  Python script that takes in a URL,
sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response."""


if __name__ == "__main__":
    from urllib.request import urlopen
    import sys

    args = sys.argv[1:]
    with urlopen(args[0]) as response:
        headers = response.info()
        X_R_ID = headers.get("X-Request-Id")
        print(X_R_ID)
