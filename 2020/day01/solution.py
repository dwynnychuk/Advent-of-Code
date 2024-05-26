import urllib
from urllib.request import urlopen
import urllib.request

# figure out reading data
""" day = 1
url = "https://adventofcode.com/2020/day/" + str(day) + "/input"
filePathSave = "input.txt"

with urlopen(url) as file:
    content = file.read().decode()

with open(filePathSave, 'w') as download:
    download.write(content) """

with open("day01/input.txt") as f:
    data = f.read().splitlines()
    data = list(map(int, data))

def part1():
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

