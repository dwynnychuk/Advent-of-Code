# Day 1 of AOC 2022
import numpy as np

with open("day01/input.txt") as f:
    data = f.read().splitlines()
    
maxelf = np.zeros([3,], dtype = int)
elf = 0
for snack in data:
    if snack != "":
        elf += int(snack)
    else:
        if elf > np.min(maxelf):
            maxelf[maxelf.argmin()] = int(elf)
        elf = 0
            

print(f"The three top elves are holding: {np.sum(maxelf)} Calories!")
