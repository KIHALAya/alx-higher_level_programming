#!/usr/bin/python3
def multiple_returns(sentence):
    str_tuple = ()
    if sentence:
        str_tuple = (len(sentence), sentence[0])
    else:
        str_tuple = (0, None)

    return (str_tuple)
