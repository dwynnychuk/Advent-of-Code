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

topElf = []
for i in range(3):
    for c, v in enumerate(elfSum):
        if v == max(elfSum):
            topElf.append(elfSum.pop(c))
            break
print(sum(topElf))
