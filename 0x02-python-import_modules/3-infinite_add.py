#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum = 0
    a = len(sys.argv)
    for i in range(a - 1):
        sum += int(sys.argv[i+1])
    print("{}".format(sum))
