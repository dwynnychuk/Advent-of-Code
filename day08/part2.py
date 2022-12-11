# AOC 2022 day 8
import numpy as np

with open("day08/input.txt") as f:
    data = f.read().splitlines()

def ScenicScore(row, column, treeArray, totRow, totCol):
    height = treeArray[row,column]
    left, right, up, down = 1, 1, 1, 1
    leftMult, rightMult, upMult, downMult = False, False, False, False

    while not leftMult:
        if column-left == 0:
            leftMult = True
            break
        elif treeArray[row, column-left] >= height:
            leftMult = True
            break
        else:
            left += 1

    while not rightMult:
        if column+right == totCol-1:
            rightMult = True
            break
        elif treeArray[row, column+right] >= height:
            rightMult = True
            break
        else:
            right += 1
    
    while not upMult:
        if row-up == 0:
            upMult = True
            break
        elif treeArray[row-up, column] >= height:
            upMult = True
            break
        else:
            up += 1
    
    while not downMult:
        if row + down == totRow-1:
            downMult = True
            break
        elif treeArray[row+down, column] >= height:
            downMult = True
            break
        else:
            down += 1
    
    score = left * right * up * down
    return score

rows = len(data)
cols = len(data[0])
trees = np.zeros((rows,cols))
visibility = np.zeros((rows, cols))

for r in range(len(data)):
    temp = list(data[r])
    for c in range(len(temp)):
        trees[r,c] = int(temp[c])

for i in range(rows):
    for j in range(cols):
        if i == 0 or j == 0 or i == (rows-1) or j == (cols-1):
            visibility[i,j] = 0
        else:
           visibility[i,j] = ScenicScore(i,j,trees,rows,cols)

print(f"\n\nThe maximum scenic score is {np.amax(visibility)}\n")

