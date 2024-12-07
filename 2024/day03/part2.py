# AOC 2024 Day 03 Part 02
import re
day = "03"
year = "2024"

global totalSum
totalSum = 0

def get_data(day, year):
    """Returns full dataset as single string"""
    data = ""
    with open(year + "/day" + day + "/input.txt") as file:
        temp = file.read().splitlines()
    for i in range(len(temp)):
        data = data + temp[i]
    return data

def make_regex(data) -> None:
    """Makes list of relevant matches that needs to be processed"""
    reList = re.findall("mul\([0-9]{1,3}\,[0-9]{1,3}\)", data)
    process_list(reList)
    
def split_strings(inputData):
    global totalSum

    while True:
        containsDont = re.search(r"don't\(\)", inputData)
        if containsDont:
            dataToProcess = inputData[:containsDont.start()]            
            print(f"Processing...\n{dataToProcess}")
            make_regex(dataToProcess)
            inputData = inputData[containsDont.end():]
            containsDo = re.search(r"do\(\)", inputData)
            if containsDo:
                inputData = inputData[containsDo.end():]
            else:
                print("Breaking: No More Starting Criteria")
                print(inputData)
                break 
        else:
            print("Breaking: No More Stopping Criteria")
            make_regex(inputData)
            break
            
    return totalSum

def process_list(mulList) -> None:
    global totalSum
    for val in mulList:
        totalSum += int(val.split(",")[0].split("(")[1]) * int(val.split(",")[1].split(")")[0])

data = get_data(day=day, year=year)
answer = split_strings(data)
print(f"The answer for part 2 is: {answer}")