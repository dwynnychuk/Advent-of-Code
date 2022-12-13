# AOC 2022 challenge day 9
import numpy as np

with open("day09/input.txt") as f:
    data = f.read().splitlines()

grid_size = 500
position_x_H, position_y_H, position_x_T, position_y_T = round(grid_size/2), round(grid_size/2), round(grid_size/2), round(grid_size/2)
data_length = len(data)
move_direction = []
move_quantity = []
visited = np.zeros((grid_size, grid_size))
visited[position_x_T, position_y_T] = 1

for d in data:
    move_direction.append(d.split()[0])
    move_quantity.append(int(d.split()[1]))

for i in range(data_length):
    for j in range(move_quantity[i]):
        if move_direction[i] == "L":
            position_x_H -= 1
        elif move_direction[i] == "R":
            position_x_H += 1
        elif move_direction[i] == "U":
            position_y_H -= 1
        elif move_direction[i] == "D":
            position_y_H += 1

        if position_x_H == position_x_T and position_y_H == position_y_T:
            print("same position")
            pass

        elif position_x_H != position_x_T and position_y_H != position_y_T:
            print("diagnal")
            if move_direction[i] == "L":
                position_x_T = position_x_H + 1
                position_y_T = position_y_H
            elif move_direction[i] == "R":
                position_x_T = position_x_H - 1
                position_y_T = position_y_H
            elif move_direction[i] == "U":
                position_y_T = position_y_H - 1
                position_x_T = position_x_H
            elif move_direction[i] == "D":
                position_y_T = position_y_H - 1
                position_x_T = position_x_H
        elif position_x_H == position_x_T or position_y_H == position_y_T:
            if np.abs(position_x_H - position_x_T) + np.abs(position_y_H - position_y_T) >= 2:
                if move_direction[i] == "L":
                    position_x_T -= 1
                elif move_direction[i] == "R":
                    position_x_T += 1
                elif move_direction[i] == "U":
                    position_y_T -= 1
                elif move_direction[i] == "D":
                    position_y_T += 1
        visited[position_x_T, position_y_T] = 1

print(sum(sum(visited)))
print(np.amax(visited))
print(sum(move_quantity))





