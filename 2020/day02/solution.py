# AOC 2020 Day 2
import numpy as np

with open("day02/input.txt") as file:
    data = file.read().splitlines()

def part1():
    count = 0
    for password in data:
        rules, letter, entry = password.split(sep = ' ')
        limits = list(map(int, rules.split(sep = '-')))
        letter = letter.split(sep=':')
        occurances = entry.count(letter[0])
        if occurances >= limits[0] and occurances <= limits[1]:
            count += 1
        else:
            count += 0
    return count

def part2():
    count = 0
    for password in data:
        rules, letter, entry = password.split(sep = ' ')
        limits = list(map(int, rules.split(sep = '-')))
        letter = letter.split(sep=':')
        letterInLocation = [entry[limits[0] - 1], entry[limits[1] - 1]]
        if (letterInLocation[0] == letter[0]) and not (letterInLocation[1] == letter[0]):
            count += 1
        elif (letterInLocation[1] == letter[0]) and not (letterInLocation[0] == letter[0]):
            count += 1
        else:
            count += 0
    return count


valid1 = part1()
valid2 = part2()
print(valid1)
print(valid2)

