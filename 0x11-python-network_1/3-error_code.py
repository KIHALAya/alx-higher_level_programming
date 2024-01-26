#!/usr/bin/python3
""" 3-error_code.py - Python script that takes in a URL,
sends a request to the URL and displays the body of the response
(decoded in utf-8)."""


if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    import sys

    args = sys.argv[1:]

    try:
        with urlopen(args[0]) as response:
            content = response.read().decode('utf-8')
            print(content)
    except HTTPError as e:
        print(f"Error code: {e.code}")
