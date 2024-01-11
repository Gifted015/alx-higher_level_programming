#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
end = number % 10
if (end > 5):
    print(f"Last digit of {number} is {end} and is greater than 5")
elif (end < 6 and end != 0):
    print(f"Last digit of {number} is {end} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {end} and is 0")
