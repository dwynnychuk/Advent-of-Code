# AOC 2022 day 11
import numpy as np
from math import floor

with open("day11/input.txt") as f:
    data = f.read().splitlines()

## Initializations
num_monkeys = 8
rounds = 20
test_nums = []
true_throw = []
false_throw = []
starting_items = []
monkey_business_array = []

## Read data
for d in data:
    if "Test: divisible by" in d:
        test_nums.append(int(d.split()[-1]))
    elif "If true:" in d:
        true_throw.append(int(d.split()[-1]))
    elif "If false:" in d:
        false_throw.append(int(d.split()[-1]))
    elif "Starting" in d:
        starting_items.append(d.split(sep=": ")[-1])

## Monkey class
class Monkey:
    def __init__(self, id):
        self.id = id
        self.worry_items = []
        self.true_throw = -1
        self.false_throw = -1
        self.inspected = 0

    def __str__(self) -> str:
        return f"Monkey #{self.id}"

def monkey_round(worry):
    return floor(worry/3)

def new_worry(worry, id):
    if id == 0:
        new_worry = worry * 7
    elif id == 1:
        new_worry = worry + 7
    elif id == 2:
        new_worry = worry * 3
    elif id == 3:
        new_worry = worry + 3
    elif id == 4:
        new_worry = worry * worry
    elif id == 5:
        new_worry = worry + 8
    elif id == 6:
        new_worry = worry + 2
    elif id == 7:
        new_worry = worry + 4
    return new_worry

# Initialize Monkeys
monkeys = [Monkey(i) for i in range(num_monkeys)]
for j in range(num_monkeys):
    monkeys[j].worry_items = list(starting_items[j].split(sep=", "))
    for k in range(len(monkeys[j].worry_items)):
        monkeys[j].worry_items[k] = int(monkeys[j].worry_items[k])
    
    monkeys[j].true_throw = true_throw[j]
    monkeys[j].false_throw = false_throw[j]

# worry level old
# inspection
# worry level new
# worry level = int(rounddown(worry/3))
# test
# throw

for round in range(rounds):
    pass




total_inspections = sorted([monkeys[i].inspected for i in range(num_monkeys)])
monkey_business_array = total_inspections[-2:]
mb = monkey_business_array[0] * monkey_business_array[1]
print(f"The level of monkey business is: {mb}\n")
