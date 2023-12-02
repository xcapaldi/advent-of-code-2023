#! /usr/bin/env python3

# Find mininum number of cubes of each color that could be used to satisfy a
# single game. Multiply the numbers for the colors to get the power. Then
# sum the powers of all the games.

sum = 0

def check_game_power(game):
    draws_string = line.split(": ")[1]
    drawings = draws_string.split("; ")

    min_population = {"red": 0, "green": 0, "blue": 0}
    for draw in drawings:
        sort = draw.split(", ")
        for s in sort:
            # strip leading or trailing then split on space between
            num, color = s.split(" ")
            # fix weird cutting off of last 'e' in 'blue'
            if color == "blu":
                color = "blue"

            if min_population[color] < int(num):
                min_population[color] = int(num)

    return min_population["red"] * min_population["green"] * min_population["blue"]

with open("2-2.txt") as file:
    while True:
        line = file.readline().strip()

        if not line:
            break

        sum += check_game_power(line)

print(sum)
