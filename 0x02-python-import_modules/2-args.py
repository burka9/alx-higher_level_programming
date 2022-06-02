#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    length = len(sys.argv) - 1
    end = 's:'

    if length == 0:
        end = 's.'
    elif length == 1:
        end = ':'

    print("{} argument{}".format(length, end))

    for i in range(length):
        print("{:d}: {}".format(i+1, sys.argv[i+1]))
