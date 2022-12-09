# AOC 2022 day 8
import numpy as np

with open("day08/input.txt") as f:
    data = f.read().splitlines()

def CheckVisibility(row, column, value):
    visible = True
    return visible

rows = len(data)
cols = len(data[0])
trees = np.zeros((rows,cols))

for r in range(len(data)):
    temp = list(data[r])
    for c in range(len(temp)):
        trees[r,c] = int(temp[c])
