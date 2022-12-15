# AOC 2022 day 11
import numpy as np

with open("day11/input.txt") as f:
    data = f.read().splitlines()
    
num_monkeys = 8
test_nums = []
true_throw = []
false_throw = []
starting_items = []

for d in data:
    if "Test: divisible by" in d:
        test_nums.append(int(d.split()[-1]))
    elif "If true:" in d:
        true_throw.append(int(d.split()[-1]))
    elif "If false:" in d:
        false_throw.append(int(d.split()[-1]))
    elif "Starting" in d:
        starting_items.append(d.split(sep=": ")[-1])

class Monkey:
    def __init__(self, id):
        self.id = id

    def __str__(self) -> str:
        return f"Monkey #{self.id}"

monkeys = [Monkey(i) for i in range(num_monkeys)]

