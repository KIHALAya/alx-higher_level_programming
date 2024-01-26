#!/usr/bin/python3
""" 2-post_email.py - Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""


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
