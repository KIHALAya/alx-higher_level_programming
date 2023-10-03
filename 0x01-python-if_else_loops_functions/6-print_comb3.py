#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):

        comb = "{}{}".format(i, j)

        if i != j:
            if i < j:

                if comb == "89":
                    print("{}".format(comb))
                else:
                    print("{}".format(comb), end=", ")
