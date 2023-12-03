# AOC 2022 day 13
with open("day13/input.txt") as f:
    data = f.read().strip().split("\n\n")

packets = []
for ind, packet in enumerate(data):
    left_right = packet.split("\n")
    packets.append((ind, eval(left_right[0]), eval(left_right[1])))

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

correct = 0

for pack in packets:
    l, r = pack[1], pack[2]
    if compare(l,r) == 1:
        correct += pack[0] + 1

print(f"The sum of correctly ordered packets is {correct}")