# Day 2 of AOC 2022
# 1 point X, 2 point Y, 3 point Z
# 0 point loss, 3 point tie, 6 point Win

with open("day02/input.txt") as f:
    data = f.read().splitlines()

elf = []
play = []
points = 0

for d in data:
    elf.append(d.split(" ")[0])
    play.append(d.split(" ")[1])

for i in range(len(elf)):
    if play[i] == "X" and elf[i] == "A":
        points += 3
        points += 1
    elif play[i] == "X" and elf[i] == "B":
        points += 0
        points += 1
    elif play[i] == "X" and elf[i] == "C":
        points += 6
        points += 1
    if play[i] == "Y" and elf[i] == "A":
        points += 6
        points += 2
    elif play[i] == "Y" and elf[i] == "B":
        points += 3
        points += 2
    elif play[i] == "Y" and elf[i] == "C":
        points += 0
        points += 2
    if play[i] == "Z" and elf[i] == "A":
        points += 0
        points += 3
    elif play[i] == "Z" and elf[i] == "B":
        points += 6
        points += 3
    elif play[i] == "Z" and elf[i] == "C":
        points += 3
        points += 3

print(points)
        
