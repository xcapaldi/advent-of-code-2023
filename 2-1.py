#! /usr/bin/env python3

# Sum game IDs of games possible if there are only 12 red cubes, 13 green cubes,
# and 14 blue cubes.

population = {"red": 12, "green": 13, "blue": 14, "blu": 14}
sum = 0

#
def check_game(game):
    line = game.strip("Game ")
    game_id, draws_string = line.split(": ")
    drawings = draws_string.split("; ")

    for draw in drawings:
        sort = draw.split(", ")
        for s in sort:
            # strip leading or trailing then split on space between
            num, color = s.split(" ")
            try:
                if population[color] < int(num):
                    return 0, False
            except:
                print(game, "--", draw, "--", s)

    return int(game_id), True


with open("2-1.txt") as file:
    while True:
        line = file.readline().strip()

        if not line:
            break

        game_id, ok = check_game(line)
        if ok:
            sum += game_id

print(sum)
