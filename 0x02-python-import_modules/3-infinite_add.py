#!/usr/bin/python3
def main():

    import sys
    args = sys.argv
    del args[0]
    lenn = len(args)
    summ = 0

    for i in range(lenn):
        summ += int(args[i])

    print(summ)


if __name__ == "__main__":
    main()
