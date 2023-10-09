#!/usr/bin/python3
def multiple_returns(sentence):
    leng_sen = len(sentence)

    if (leng_sen == 0):
        new_tuple = (leng_sen, None)
    else:
        new_tuple = (leng_sen, sentence[0])

    return (new_tuple)
