# AOC 2022 challenge day 9
import numpy as np

with open("day09/input.txt") as f:
    data = f.read().splitlines()

grid_size = 3000
position_x, position_y = round(grid_size/2), round(grid_size/2)
data_length = len(data)
move_direction = []
move_quantity = []
visited = np.zeros((grid_size, grid_size))
visited[position_x, position_y] = 1

for d in data:
    move_direction.append(d.split()[0])
    move_quantity.append(int(d.split()[1]))

for i in range(data_length):
    if move_direction == "L":
        pass
    elif move_direction == "R":
        pass
    elif move_direction == "U":
        pass
    elif move_direction == "D":
        pass
    



