#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of
the response  """

if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv
    email = {'email': argv[2]}
    encoding = parse.urlencode(email)
    data = encoding.encode('ascii')
    with request.urlopen(argv[1], data) as response:
        body = response.read()
        print(body.decode('utf-8'))
