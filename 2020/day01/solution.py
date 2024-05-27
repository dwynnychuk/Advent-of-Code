# AOC 2020 Day 1
with open("day01/input.txt") as f:
    data = f.read().splitlines()
    data = list(map(int, data))

def part1():
    # Part 1 solution
    for entry1 in data:
        for entry2 in data:
            sum = entry1 + entry2
            if sum == 2020:
                product = entry1 * entry2
                return product
            
def part2():
    # Part 2 solution
    for entry1 in data:
        for entry2 in data:
            for entry3 in data:
                sum = entry1 + entry2 + entry3
                if sum == 2020:
                    product = entry1 * entry2 * entry3
                    return product
            
solution1 = part1()
solution2 = part2()

print("The solution to part 1 is: " + str(solution1) + "!")
print("The solution to part 2 is: " + str(solution2) + "!")
# End

if __name__ == "__main__":
    ...
