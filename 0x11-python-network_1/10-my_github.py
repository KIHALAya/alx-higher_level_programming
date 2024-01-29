#!/usr/bin/python3
""" 10-my_github.py - Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    args = sys.argv[1:]
    url = f"https://api.github.com/user"
    auth = HTTPBasicAuth(args[0], args[1])

    response = requests.get(url, auth=auth)

    user_data = response.json()
    user_id = user_data.get("id")
    print(user_id)
