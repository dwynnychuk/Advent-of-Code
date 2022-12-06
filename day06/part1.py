# AOC Day 6 2022
with open("day06/input.txt") as f:
    data = f.read()

s = list(data)

for d in range(4000):
    four = s[d:(d+4)]
    f_4 = four.pop()
    if f_4 in four:
        print("duplicate")
        continue
    f_3 = four.pop()
    if f_3 in four:
        print("triplicate")
        continue
    f_2 = four.pop()
    if f_2 in four:
        print("quadrupilcate")
        continue
    print(f"Passed {d+4}")
    break
    

