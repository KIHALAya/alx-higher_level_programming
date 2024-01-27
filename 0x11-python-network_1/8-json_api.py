#!/usr/bin/python3
""" 8-json_api.py - Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter"""


if __name__ == "__main__":
    import requests
    import sys

    args = sys.argv[1:]

    if args:
        q = args[0]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": q})

    try:
        jsn_body = response.json()
        if jsn_body == {}:
            print("No result")
        else:
            print("[{}] {}".format(jsn_body.get("id"), jsn_body.get("name")))
    except ValueError:
        print("Not a valid JSON")
