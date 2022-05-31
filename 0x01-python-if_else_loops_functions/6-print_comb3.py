#!/bin/usr/python3
for i in range(10):
    for j in range(i+1, 10):
        if (i is not j):
            print(f"{i:d}{j:d}", end=", ")
print()
