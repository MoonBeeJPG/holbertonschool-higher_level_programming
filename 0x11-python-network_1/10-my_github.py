#!/usr/bin/python3
""" Python script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id """

if __name__ == "__main__":
    import requests
    from sys import argv
    user = argv[1]
    passw = argv[2]
    response = requests.get('https://api.github.com/user', auth=(user, passw))
    data = response.json()
    try:
        print(data['id'])
    except Exception:
        print("None")
