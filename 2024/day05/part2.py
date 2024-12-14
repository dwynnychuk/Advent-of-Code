# AOC 2024 Day 05 Part 02

from functools import cmp_to_key

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

def define_rules(rulesInput):
    return [tuple(map(int, rule.split("|"))) for rule in rulesInput if "|" in rule]

dataRules, dataUpdates = get_data(day, year)
rules = define_rules(dataRules)

def parse_updates(rules, dataUpdates):
    global totalSum
    for strUpdate in dataUpdates:
        update = list(map(int, strUpdate.split(",")))
        badFlag = False
        for i in range(len(rules)):
            if rules[i][0] in update and rules[i][1] in update and update.index(rules[i][0]) > update.index(rules[i][1]):
                order_update(update, rules)
                break

def order_update(update, rules):
    global totalSum
    
    def modified_compare(a, b):
        if ((a,b) in rules):
            return -1
        elif ((b,a) in rules):
            return 1
        else:
            return 0
        
    newUpdate = sorted(update, key=cmp_to_key(modified_compare))
    print(newUpdate)
    totalSum += newUpdate[int((len(newUpdate)-1)/2)]

parse_updates(rules, dataUpdates)
print(f"\nThe total of the middle updates passing the test is: {totalSum}\n")