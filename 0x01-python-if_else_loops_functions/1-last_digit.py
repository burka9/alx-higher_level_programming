#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if last > 5:
    lastStr = "and is greater than 5"
elif last == 0:
    lastStr = "and is 0"
else:
    lastStr = "and is less than 6 and not 0"
str = f"Last digit of {number:d} is {last:d} {lastStr}"
print(str)
