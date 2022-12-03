# Day 03 of AOC 2022

with open("day03/input.txt") as f:
    data = f.read().splitlines()

priorities = 0
alphabetOffset = 26
commonItems = []

lowerDict = {
    "a": 1, "b": 2, "c":3, "d":4, "e": 5,
    "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
    "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
    "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
    "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
    }

for d in data:
    itemNum = int(len(d)/2)
    for i in range(itemNum):
        if d.find(d[i],itemNum) != -1:
            commonItems.append(d[i])
            break


for c in commonItems:
    if c.isupper():
        priorities += lowerDict[c.lower()] + 26
    elif c.islower():
        priorities += lowerDict[c]

print(f"The total priority sum is: {priorities}!")