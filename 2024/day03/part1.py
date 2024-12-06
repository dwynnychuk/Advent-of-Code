# AOC 2024 Day 03 Part 01
import re
day = "03"
year = "2024"

def get_data(day, year):
    with open(year + "/day" + day + "/input.txt") as file:
        data = file.read().splitlines()
    return data

def make_regex(data) -> list:
    mulList = []
    for i in range(len(data)):
        mulListTemp = re.findall("mul\([0-9]{1,3}\,[0-9]{1,3}\)",data[i])
        mulList = mulList + mulListTemp
    return mulList

def process_list(mulList) -> int:
    totalSum = 0
    for val in mulList:
        totalSum += int(val.split(",")[0].split("(")[1]) * int(val.split(",")[1].split(")")[0])
    return totalSum

data = get_data(day=day, year=year)
mulList = make_regex(data)
answer = process_list(mulList)
print(f"The answer for part 1 is: {answer}")