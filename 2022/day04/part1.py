# Day 04 of AOC 2022
with open("day04/input.txt") as f:
    data = f.read().splitlines()

contained = 0

for d in data:
    s1, s2 = d.split(",")
    s1_s, s1_e = s1.split("-")
    s2_s, s2_e = s2.split("-")
    if int(s1_s) <= int(s2_s) and int(s1_e) >= int(s2_e):
        contained += 1
    elif int(s2_s) <= int(s1_s) and int(s2_e) >= int(s1_e):
        contained += 1

print(f"The number of fully contained zones is: {contained}.")