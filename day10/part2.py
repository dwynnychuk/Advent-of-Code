# AOC 2022 day 10
with open("day10/input.txt") as f:
    data = f.read().splitlines()

def check_cycle(current_row, cycle):
    """ Check to see if current row is full. If it is, print and reset row and cycle"""
    if cycle == 41:
        print(''.join(current_row))
        current_row = []
        cycle = 1
        return current_row, cycle
    else:
        return current_row, cycle

def print_char(cycle, X):
    sprite = [X-1, X, X+1]
    if cycle in sprite:
        char_to_print = '#'
    else:
        char_to_print = '.'
    return char_to_print

# begin or continue
# draw pixel
# move register
# increase position

X = 1
cycle = 1
current_row = []

for d in data:

    if d.startswith("noop"):
        current_row, cycle = check_cycle(current_row, cycle)
        char_to_print = print_char(cycle,X)
        current_row.append(char_to_print)
        cycle += 1

    elif d.startswith("addx"):
        V = int(d.split()[1])

        current_row, cycle = check_cycle(current_row, cycle)
        char_to_print = print_char(cycle, X)
        current_row.append(char_to_print)
        cycle += 1
        current_row, cycle = check_cycle(current_row, cycle)
        char_to_print = print_char(cycle, X)
        current_row.append(char_to_print)
        X += V
        cycle += 1