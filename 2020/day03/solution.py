# AOC 2020 Day 3
with open("day03/input.txt") as file:
    data = file.read().splitlines()

def part1():
    right = -3
    count = 0
    for line in data:
        right += 3
        if right >= len(line):
            right = right - len(line)
        char = line[right]
        if ord(char) == 35:
            count += 1
    return count

def part2(rightSteps, downSteps):
    right = -1 * rightSteps
    count = 0
    for i, line in enumerate(data):
        if i % downSteps != 0:
            continue
        right += rightSteps
        if right >= len(line):
            right = right - len(line)
        char = line[right]
        if ord(char) == 35:
            count += 1
    return count

rs = [1, 3, 5, 7, 1]
ds = [1, 1, 1, 1, 2]
product = 1

for j in range(len(rs)):
    product = product * part2(rs[j], ds[j])

print("The solution to part 1 is: " + str(part1()))
print("The solution to part 2 is: " + str(product))
# End
