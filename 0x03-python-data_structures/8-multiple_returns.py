#!/usr/bin/python3
def multiple_returns(sentence):
    lent = len(sentence)
    if sentence:
        beg = sentence[0]
    else:
        beg = None
    return (lent, beg)
