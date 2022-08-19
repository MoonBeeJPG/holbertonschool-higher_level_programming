#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """

if __name__ == "__main":
    import requests
    response = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(response))
    print("\t- content: {}".format(response.content))
