#Day 05 of AOC2022
with open("day05/input.txt") as f:
    data = f.read().splitlines()

initialEnd = 8
dataStart = 10

one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []

for d in data[0:initialEnd]:
    one.append(d[1:2])
    two.append(d[5:6])
    three.append(d[9:10])
    four.append(d[13:14])
    five.append(d[17:18])
    six.append(d[21:22])
    seven.append(d[25:26])
    eight.append(d[29:30])
    nine.append(d[33:34])

one.reverse()
two.reverse()
three.reverse()
four.reverse()
five.reverse()
six.reverse()
seven.reverse()
eight.reverse()
nine.reverse()

quantity = []
old = []
new = []

for l in data[dataStart:dataStart+3]:
    _, q, _, o, _, n = l.split(" ")
    quantity.append(q)
print(quantity)