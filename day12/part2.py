# AOC 2022 day 12
import numpy as np
from heapq import heappush, heappop

with open("day12/input.txt") as f:
    data = f.read().splitlines()

rows = len(data)
cols = len(data[0])
elevations = np.zeros((rows,cols))

for r in range(rows):
    for c in range(cols):
        e = data[r][c]
        match e:
            case "S":
                e = "a"
            case "E":
                start = (r,c)
                e = "z"
        elevations[r][c] = ord(e) - 97

#find neighboring points
def find_neighbours(row, column):
    for d_row, d_col in [[1,0],[-1,0],[0,-1],[0,1]]:
        new_row = row + d_row
        new_col = column + d_col

        if not (0 <= new_row < rows and 0 <= new_col < cols):
            continue

        if elevations[new_row][new_col] + 1 >= elevations[row][column]:
            yield new_row, new_col

visited = np.zeros((rows,cols), dtype=bool)
heap = [(0, start[0], start[1])]

#dijkstra
while True:
    cost, i, j = heappop(heap)

    if visited[i][j]:
        continue
    visited[i][j] = True

    if elevations[i][j] == 0:
        print(f"The total steps taken was: {cost}")
        break

    for nr, nc in find_neighbours(i, j):
        heappush(heap, (cost + 1, nr, nc))