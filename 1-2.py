#!/usr/bin/env python3

sum = 0

with open("1-2.txt") as file:
    while True:
        line = file.readline()

        if not line:
            break

        number = ""

        # replace numbers spelled as words with digits
        one = line.replace("one", "1")
        two = line.replace("two", "2")
        three = line.replace("three", "3")
        four = line.replace("four", "4")
        five = line.replace("five", "5")
        six = line.replace("six", "6")
        seven = line.replace("seven", "7")
        eight = line.replace("eight", "8")
        nine = line.replace("nine", "9")

        # find leftmost digit from each
        leftmost_index = -1
        leftmost_char = ""
        for replacement in [one, two, three, four, five, six, seven, eight, nine]:
            for i, char in enumerate(replacement):
                if char.isdigit() and (i < leftmost_index or leftmost_index == -1):
                    leftmost_index = i
                    leftmost_char = char
                    break

        number += leftmost_char

        # find rightmost digit from each
        leftmost_index = -1
        leftmost_char = ""

        for replacement in [one, two, three, four, five, six, seven, eight, nine]:
            for i, char in enumerate(replacement[::-1]):
                if char.isdigit() and (i < leftmost_index or leftmost_index == -1):
                    leftmost_index = i
                    leftmost_char = char
                    break


        number += leftmost_char

        sum += int(number)

print(sum)

