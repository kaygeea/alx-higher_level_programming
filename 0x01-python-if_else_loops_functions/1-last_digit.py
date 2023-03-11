#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldg = abs(number) % 10
if number < 0:
    print(f"Last digit of {number} is -{ldg} and is less than 6 and not 0")
elif number >= 0:
    if ldg > 5:
        print(f"Last digit of {number} is {ldg} and is greater than 5")
    elif ldg == 0:
        print(f"Last digit of {number} is {ldg} and is 0")
    elif ldg < 6 and last_dig != 0:
        print(f"Last digit of {number} is {ldg} and is less than 6 and not 0")
