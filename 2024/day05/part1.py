# AOC 2024 Day 05 Part 01
day = "05"
year = "2024"

global totalSum
totalSum = 0

def get_data(day, year):
    with open(year + "/day" + day + "/input.txt") as file:
        data = file.read().split("\n\n")
        rules = data[0].split("\n")
        updates = data[1].split("\n")
    return rules, updates

def define_rules(rules):
    first = []
    second = []
    for rule in rules:
        first.append(int(rule.split("|")[0]))
        second.append(int(rule.split("|")[1]))
    return first, second
    
def parse_updates(first, second, dataUpdates):
    global totalSum
    for strUpdate in dataUpdates:
        update = list(map(int, strUpdate.split(",")))
        badFlag = False
        for i in range(len(first)):
            if first[i] in update and second[i] in update and update.index(first[i]) < update.index(second[i]):
                continue
            elif first[i] in update and second[i] in update and update.index(first[i]) > update.index(second[i]):
                badFlag = True
                break
        if not badFlag:
            totalSum += update[int((len(update)-1)/2)]

dataRules, dataUpdates = get_data(day, year)
first, second = define_rules(dataRules)
parse_updates(first, second, dataUpdates)
print(f"\nThe total of the middle updates passing the test is: {totalSum}\n")