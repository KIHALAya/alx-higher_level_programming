#!/usr/bin/python3
def main():
    import hidden_4
    content = dir(hidden_4)
    for each in content:
        if each[:2] != "__":
            print(each)


if __name__ == "__main__":
    main()
