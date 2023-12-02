#!/usr/bin/env python3

sum = 0

with open("1-1.txt") as file:
    while True:
        line = file.readline()

        if not line:
            break

        number = ""

        for char in line:
            if char.isdigit():
                number += char
                break

        # step backward through the string
        for char in line[::-1]:
            if char.isdigit():
                number += char
                break

        sum += int(number)

print(sum)

