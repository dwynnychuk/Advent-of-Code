# AOC 2024 DAY 01 PART 01
import operator

year = "2024"
day = "01"

def get_data(day, year):
    with open(year + "/day" + day + "/input.txt") as file:
        data = file.read().splitlines()
        print(data)
    return data

def create_lines(data):
    left = []
    right = []
    for lines in data:
        left.append(int(lines.split("   ")[0]))
        right.append(int(lines.split("   ")[1]))
    left.sort()
    right.sort()
    return left, right

def get_difference(left, right):
    difference = []
    for idx in range(len(left)):
        difference.append(abs(left[idx] - right[idx]))
    return difference

data = get_data(day, year)
left, right = create_lines(data)
difference = get_difference(left, right)

answer = sum(difference)
print(answer)