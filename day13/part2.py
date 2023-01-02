# AOC 2022 day 13
# go through all packets and find those less than 2 and those less than 6
with open("day13/input.txt") as f:
    data = f.read().strip().split("\n\n")

packets = []

for packet in data:
    left_right = packet.split("\n")
    packets.append(eval(left_right[0]))
    packets.append(eval(left_right[1]))

def compare(first, lessthan2, lessthan6):
    if isinstance(first, list):
        count = 0
        while count < len(first):
            result = compare(first[count], lessthan2, lessthan6)

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
        
    if isinstance(first, int):
        if first == 6:
            print("6")
        if first < 6:
            lessthan6 += 1
            if first < 2:
                lessthan2 += 1
            if first == 2:
                print("2")
            return 1
    return -1

lessthan2 = 1
lessthan6 = 1

# for pack in packets:
#     l, r = pack[1], pack[2]
#     if compare(l,r) == 1:
#         correct += pack[0] + 1

# print(f"The sum of correctly ordered packets is {correct}")
