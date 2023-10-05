#!/usr/bin/python3
def main():
    import sys
    args = sys.argv[1:]
    lenn = len(args)

    if lenn == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(lenn))
        for i in range(lenn):
            print("{}: {}".format(i, args[i]))


if __name__ == "__main__":
    main()
