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


diskSpace = 70000000
unusedSpaceRequired = 30000000
totalAllowedToUse = diskSpace-unusedSpaceRequired
totalUsedSpace = dirSize["/"]
requiredToFree = totalUsedSpace-totalAllowedToUse
largeFiles = []

for i in dirSize.values():
    if i >= requiredToFree:
        largeFiles.append(i)

fileToPop = sorted(largeFiles)[0]
print(f"The directory to delete has a size of {fileToPop}")