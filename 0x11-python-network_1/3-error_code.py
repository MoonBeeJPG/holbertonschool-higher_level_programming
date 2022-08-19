#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
    and displays the body of the response """

if __name__ == "__main__":
    from urllib import request, error
    from sys import argv
    try:
        with request.urlopen(argv[1]) as response:
            body = response.read()
            print(body)
    except error.HTTPError as error:
        print(error.code)
