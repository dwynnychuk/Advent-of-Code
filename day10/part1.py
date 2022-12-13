# AOC 2022 day 10
with open("day10/input.txt") as f:
    data = f.read().splitlines()

def check_cycle(cycles_of_interest, signal_strength, cycle, X):
    if cycle in cycles_of_interest:
        signal_strength.append(cycle * X)
        return True
    else:
        return True

cycles_of_interest = [20, 60, 100, 140, 180, 220]
signal_strength = []

X = 1
cycle = 1

for d in data:
    if d.startswith("noop"):
        cycle += 1
        check_cycle(cycles_of_interest, signal_strength, cycle, X)
    elif d.startswith("addx"):
        V = int(d.split()[1])
        cycle += 1
        check_cycle(cycles_of_interest, signal_strength, cycle, X)
        cycle += 1
        X += V
        check_cycle(cycles_of_interest, signal_strength, cycle, X)

ans = sum(signal_strength)
print(f"The sum of the signal strength is {ans}")