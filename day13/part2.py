# AOC 2022 day 13
# go through all packets and find those less than 2 and those less than 6
from xml.etree.ElementTree import iselement


with open("day13/input.txt") as f:
    data = f.read().strip().split("\n\n")

packets = []

for packet in data:
    left_right = packet.split("\n")
    packets.append(eval(left_right[0]))
    packets.append(eval(left_right[1]))

def compare(first, lessthan2, lessthan6):
    if isinstance(first, list):
        if first:
            lessthan2, lessthan6 = compare(first[0], lessthan2, lessthan6)
        else:
            lessthan2 += 1
            lessthan6 += 1
            return lessthan2, lessthan6

    if isinstance(first, int):
        if first == 6:
            print("6")
        if first < 6:
            lessthan6 += 1
            if first < 2:
                lessthan2 += 1
            if first == 2:
                print("2")
            return lessthan2, lessthan6

lessthan2 = 1
lessthan6 = 1
for pack in packets:
    lessthan2, lessthan6 = compare(pack, lessthan2, lessthan6)

print(f"The number of packets less than 2 and 6 is {lessthan2} and {lessthan6} giving product {lessthan2 * lessthan6}")
