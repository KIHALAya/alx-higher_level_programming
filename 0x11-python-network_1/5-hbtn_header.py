#!/usr/bin/python3
""" 5-hbtn_header.py - Python script that takes in a URL,
sends a request to the URL and displays the value of the
variable X-Request-Id in the response header"""


if __name__ == "__main__":
    import requests
    import sys

    args = sys.argv[1:]
    url = args[0]
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
