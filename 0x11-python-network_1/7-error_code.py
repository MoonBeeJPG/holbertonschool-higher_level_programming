#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and
    displays the body of the response """

if __name__ == "__main__":
    import requests
    from sys import argv
    response = requests.get(argv[1])
    if response:
        print(response.text)
    else:
        print("Error code:", response.status_code)
