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

array = [one, two, three, four, five, six, seven, eight, nine]
for r in array:
    while(" " in r):
        r.remove(" ")

quantity = []
old = []
new = []

for l in data[dataStart:]:
    _, q, _, o, _, n = l.split(" ")
    quantity.append(q)
    old.append(o)
    new.append(n)

for lines in range(len(quantity)):
    transfer = []
    fRow = int(old[lines]) - 1
    tRow = int(new[lines]) - 1
    for q in range(int(quantity[lines])):
        transfer.append(array[fRow].pop())
    transfer.reverse()
    for t in range(len(transfer)):
        array[tRow].append(transfer[t])


winner = []

for w in range(9):
    winner.append(array[w][-1])
print(winner)