# AOC 2022 day 13
from functools import cmp_to_key


with open("day13/input.txt") as f:
    data = f.read().strip().replace("\n\n", "\n").split("\n")

packets = []
for packet in data:
    packets.append(eval(packet))

def compare(l, r):
    if isinstance(l, int) and isinstance(r, list):
        l = [l]
    if isinstance(l, list) and isinstance(r, int):
        r = [r]
    
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return 1
        if l == r:
            return 0
        return -1

    if isinstance(l, list) and isinstance(r, list):
        count = 0
        while count < len(l) and count < len(r):
            result = compare(l[count],r[count])

            if result == 1:
                return 1
            if result == -1:
                return -1

            count += 1

        if count == len(l):
            if len(l) == len(r):
                return 0
            return 1

        return -1

packets.append([[2]])
packets.append([[6]])
packets = sorted(packets, key=cmp_to_key(compare), reverse = True)
for index, pack in enumerate(packets):
    if pack == [[2]]:
        lessthan2 = index + 1
    if pack == [[6]]:
        lessthan6 = index + 1

print(f"\nThe index of [[2]] and [[6]] are {lessthan2} and {lessthan6} with a product of {lessthan2 * lessthan6}\n")
