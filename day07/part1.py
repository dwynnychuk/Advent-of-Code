# AOC day 7 2022
with open("day07/input.txt") as f:
    data = f.read().splitlines()

# data = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k"""


dirSize = {}
folders = []
curPath = []

for line in data:
    if line.startswith("$ cd"):
        if line.startswith("$ cd /"):
            pass
        elif line.startswith("$ cd .."):
            pass
        else:
            pass

    if line[0].isdigit():
        fileSize = int(line.split(' ')[0])
        for dir in folders:
            dirSize[dir] += fileSize

