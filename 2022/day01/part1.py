# Day 1 of AOC 2022

with open("day01/input.txt") as f:
    data = f.read().splitlines()
    
maxelf = 0
elf = 0
for snack in data:
    if snack != "":
        elf += int(snack)
    else:
        maxelf = max(maxelf, elf)
        elf = 0

print(f"Max elf is holding: {maxelf} Calories!")
