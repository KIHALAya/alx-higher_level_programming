#!/usr/bin/python3
""" 7-error_code.py - Python script that takes in a URL,
sends a request to the URL and displays the body of the response."""


if __name__ == "__main__":
    import requests
    import sys

    args = sys.argv[1:]
    url = args[0]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
