#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if (ord('z') - i) % 2 == 0:
        print("{}".format(chr(i)), end='')
    else:
        print("{}".format(chr(i - ord('a') + ord('A'))), end='')
