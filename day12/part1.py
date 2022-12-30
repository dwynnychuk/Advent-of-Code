# AOC 2022 day 12
import numpy as np
from heapq import heappush, heappop

with open("day12/input.txt") as f:
    data = f.read().splitlines()

rows = len(data)
cols = len(data[0])
elevations = np.zeros((rows,cols))

minimums = []

for r in range(rows):
    for c in range(cols):
        e = data[r][c]
        match e:
            case "S":
                start = (r,c)
            case "E":
                end = (r,c)

def find_elevation(char):
    if char == "S":
        elevation = 0
    elif char == "E":
        elevation = 25
    else:
        elevation = ord(char) - 97
    return elevation

def find_neighbours(row, column):
    for d_row, d_col in [[1,0],[-1.,0],[0,-1],[0,1]]:
        new_row = row + d_row
        new_col = column + d_col