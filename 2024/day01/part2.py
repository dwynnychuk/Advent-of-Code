# AOC 2024 DAY 01 PART 02
import operator

year = "2024"
day = "01"

def get_data(day, year):
    with open(year + "/day" + day + "/input.txt") as file:
        data = file.read().splitlines()
    return data

def create_lines(data):
    left = []
    right = []
    for lines in data:
        left.append(int(lines.split("   ")[0]))
        right.append(int(lines.split("   ")[1]))
    return left, right

def get_similarity(left, right):
    similarity = []
    for idx in range(len(left)):
        similarity.append(left[idx] * right.count(left[idx]))
    return similarity

def get_answer(similarity):
    answer = sum(similarity)
    print(f"The answer is: {answer}")

data = get_data(day, year)
left, right = create_lines(data)
similarity = get_similarity(left, right)
get_answer(similarity)
