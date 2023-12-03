# Day 1 of AOC 2022

with open("day01/input.txt") as f:
    data = f.read().splitlines()

elfSum = []
currentSum = 0

for d in data:
    if d == '':
        elfSum.append(currentSum)
        currentSum = 0
    else:
        currentSum += float(d)

print(max(elfSum))
