# AOC day 7 2022
from ast import Add


with open("day07/input.txt") as f:
    data = f.read().splitlines()

def AddPath(path,dir):
    if path not in dir.keys():
        dir[path] = 0
    return dir

dirSize = {}
folders = []
curPath = ""

for line in data:
    if line.startswith("$ cd"):
        if line.startswith("$ cd /"):
            curPath = "/"
            folders = ["/"]
            dirSize = AddPath(curPath,dirSize)

        elif line.startswith("$ cd .."):
            curPath = "/".join(curPath.split("/")[:-1])
            folders.pop()

        else:
            if curPath == "/":
                curPath += line.split()[-1]
            else:
                curPath += "/" + line.split()[-1]
            folders.append(curPath)
            dirSize = AddPath(curPath,dirSize)


    if line[0].isdigit():
        fileSize = int(line.split(' ')[0])
        for dir in folders:
            dirSize[dir] += fileSize

largeFiles = []
for i in dirSize.values():
    if i < 100000:
        largeFiles.append(i)

print(f"The sum of all files less than size 100,000 is {sum(largeFiles)}")