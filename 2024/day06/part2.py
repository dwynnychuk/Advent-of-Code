# AOC 2024 Day 06 Part 02
day = "06"
year = "2024"

def get_data(day, year):
    with open(year + "/day" + day + "/input.txt") as file:
        data = file.read().splitlines()
    
    directions = [(-1, 0),  # up
                  (0, 1),   # right
                  (1, 0),   # down
                  (0, -1)]  # left
    
    allowedSet = set()
    seenSet = set()
    maxRow = len(data)
    maxCol = len(data[0])
    currentDirection = 0
    
    for row, line in enumerate(data):
        for col, _ in enumerate(line):
            if line[col] == ".":
                allowedSet.add((row, col))
            elif line[col] == "^":    
                rowStart = row
                colStart = col
                allowedSet.add((row,col))
            elif line[col] == "#":
                continue
            else:
                print(f"Unknown input ({row}, {col}: {line[col]})")
                
    return rowStart, colStart, allowedSet, seenSet, directions, currentDirection, maxRow, maxCol

def turn_right(currentDirection):
    return (currentDirection + 1) % 4  # 4 directions
    
def walk_forward(oldRow, oldCol, currentDirection, directions):
    row = oldRow + directions[currentDirection][0]
    col = oldCol + directions[currentDirection][1]
    return row, col

def find_solution(rowStart, colStart, maxRow, maxCol, allowedSet, seenSet, currentDirection, directions):
    totalLoops = 0
    for omit in allowedSet:
        if omit == (rowStart, colStart):
            print("first")
            continue
        r = rowStart
        c = colStart
        currentDirection = 0
        tempAllowedSet = allowedSet.copy()
        tempAllowedSet.remove(omit)
        seenSet = set()
        while(True):
            tempRow, tempCol = walk_forward(r, c, currentDirection, directions)
            if (0 <= tempRow < maxRow) and (0 <= tempCol < maxCol):
                if (tempRow, tempCol) in tempAllowedSet:
                    if ((tempRow, tempCol, currentDirection) in seenSet):
                        totalLoops += 1
                        print((tempRow, tempCol, currentDirection, totalLoops))
                        break
                    else:
                        seenSet.add((tempRow, tempCol, currentDirection))
                        r = tempRow
                        c = tempCol
                        #print(f"new {(tempRow, tempCol, currentDirection)}")
                else:
                    currentDirection = turn_right(currentDirection)
            else:
                print(f"out {totalLoops}")
                break   
    return totalLoops  

        

rowStart, colStart, allowedSet, seenSet, directions, currentDirection, maxRow, maxCol = get_data(day, year)
totalLoops = find_solution(rowStart, colStart, maxRow, maxCol, allowedSet, seenSet, currentDirection, directions)
print(f"Solution: {totalLoops}")