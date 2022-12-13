# AOC 2022 challenge day 9
# code credit: @leej11 on github
from os import X_OK
import numpy as np
import copy

with open("day09/input.txt") as f:
    data = f.read().splitlines()

move_direction = []
move_quantity = []

for d in data:
    move_direction.append(d.split()[0])
    move_quantity.append(int(d.split()[1]))

class Knot:
    def __init__(self, id):
        self.id = id
        self.pos = [0,0]
        self.pos_visited = [[0,0]]
    
    def __str__(self):
        return f"Knot #{self.id}"

    def move(self, direction):
        self.previous_pos = copy.deepcopy(self.pos)

        if direction == "L":
            self.pos[0] -= 1
        elif direction == "R":
            self.pos[0] += 1
        elif direction == "U":
            self.pos[1] -= 1
        elif direction == "D":
            self.pos[1] += 1
        else:
            print("error")

        self.pos_visited.append(copy.deepcopy(self.pos))
    
    def update_position(self, new_position):
        self.previous_pos = copy.deepcopy(self.pos)
        self.pos = new_position
        self.pos_visited.append(new_position)

    def distinct_positions(self):
        return set(tuple(pos) for pos in self.pos_visited)


def update_all_positions(knots, direction):
    for i in range(len(knots)):

        if i == 0:
            knots[i].move(direction)
            continue

        delta_x = knots[i-1].pos[0] - knots[i].pos[0]
        delta_y = knots[i-1].pos[1] - knots[i].pos[1]

        if abs(delta_x) > 1 or abs(delta_y) > 1:
            delta_x_dir = -1 if delta_x < 0 else 1
            delta_y_dir = -1 if delta_y < 0 else 1

            if delta_x == 0:
                x_new = copy.deepcopy(knots[i].pos[0])
                y_new = copy.deepcopy(knots[i].pos[1]) + (1*delta_y_dir)
                knots[i].update_position([x_new, y_new])

            elif delta_y == 0:
                x_new = copy.deepcopy(knots[i].pos[0]) + (1*delta_x_dir)
                y_new = copy.deepcopy(knots[i].pos[1])
                knots[i].update_position([x_new, y_new])
            
            else:
                x_new = copy.deepcopy(knots[i].pos[0]) + (1*delta_x_dir)
                y_new = copy.deepcopy(knots[i].pos[1]) + (1*delta_y_dir)
                knots[i].update_position([x_new, y_new])

tail_visited = [[0,0]]
knots = []
number = 10
knots = [Knot(i) for i in range(number)]

for m in range(len(move_direction)):
    for _ in range(move_quantity[m]):
        update_all_positions(knots, move_direction[m])

ans = len(knots[-1].distinct_positions())
print(f"The number of positions visited by tail is: {ans}")


