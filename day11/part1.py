# AOC 2022 day 11
with open("day11/input.txt") as f:
    data = f.read().splitlines()

print(data)

class Monkey:
    def __init__(self, id):
        self.id = id

    def __str__(self) -> str:
        return f"Monkey #{self.id}"

m1 = Monkey(1)

print(m1)
print(m1.id)