#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return 0, None
    else:
        for i in range(len(sentence)):
            a = sentence[0]
            b = len(sentence)
        return b, a
