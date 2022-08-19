#!/usr/bin/python3
"""  Python script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter """

if __name__ == "__main__":
    import requests
    from sys import argv
    if len(argv) > 1:
        letter = {'q': argv[1]}
    else:
        letter = {'q': ""}
    response = requests.post('http://0.0.0.0:5000/search_user', letter)
    try:
        formatt = response.json()
        if len(formatt) == 0:
            print("No result")
        else:
            print("[{}] {}".format(formatt["id"], formatt["name"]))
    except TypeError:
        print("Not a valid JSON")
