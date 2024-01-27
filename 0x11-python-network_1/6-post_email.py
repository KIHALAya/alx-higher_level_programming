#!/usr/bin/python3
""" 6-post_email.py - Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response."""


if __name__ == "__main__":
    import requests
    import sys

    args = sys.argv[1:]
    url = args[0]
    email = {"email": args[1]}
    response = requests.post(url, data=email)
    print(response.text)
