# AOC 2022 day 8
import numpy as np

with open("day08/input.txt") as f:
    data = f.read().splitlines()

def CheckVisibility(row, column, treeArray, totRow, totCol):
    height = treeArray[row,column]
    visL = True
    # check left
    for l in range(column):
        if treeArray[row,l] >= height:
            visL = False
            break
        else:
            continue
    if visL:
        return True


    # check right
    visR = True
    for r in range(column+1, totCol):
        if treeArray[row,r] >= height:
            visR = False
            break
        else:
            continue
    if visR:
        return True

    # check up
    visU = True
    for u in range(row):
        if treeArray[u,column] >= height:
            visU = False
            break
        else:
            continue
    if visU:
        return True

    # check down
    visD = True
    for d in range(row+1, totRow):
        if treeArray[d, column] >= height:
            visD = False
            break
        else:
            continue
    if visD:
        return True
    else:
        return False


rows = len(data)
cols = len(data[0])
trees = np.zeros((rows,cols))
visible = 0

for r in range(len(data)):
    temp = list(data[r])
    for c in range(len(temp)):
        trees[r,c] = int(temp[c])

for i in range(rows):
    for j in range(cols):
        if i == 0 or j == 0 or i == (rows-1) or j == (cols-1):
            visible += 1
        else:
            if CheckVisibility(i,j,trees,rows,cols):
                visible += 1
            
print(f"\n\nThe total number of visible trees is {visible}\n")

