#!/usr/bin/python3
def uppercase(str):
    up_str = ""
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            up = chr(ord(i) - ord('a') + ord('A'))
        else:
            up = i
        up_str += up
    print(up_str)
