# AOC Day 6 2022
with open("day06/input.txt") as f:
    data = f.read()

lstr = 14
s = list(data)
answer = []

for d in range(len(s)):
    strip = s[d:(d+lstr)]
    for p in range(len(strip)):
        if strip.count(strip[p]) > 1:
            break
        elif p == (len(strip) - 1):
            answer.append(d+lstr)
            break

print(answer)

    

