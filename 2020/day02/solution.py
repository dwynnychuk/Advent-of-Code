# AOC 2020 Day 2
import operator

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
        if operator.xor((letterInLocation[1] == letter[0]), (letterInLocation[0] == letter[0])):
            count += 1
        else:
            count += 0
    return count

valid1 = part1()
valid2 = part2()

print("The solution to Part 1 is: " + str(valid1))
print("The solution to Part 2 is: " + str(valid2))
# End