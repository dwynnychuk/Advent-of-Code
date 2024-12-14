# AOC 2024 Day 06 Part 01
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
    r = rowStart
    c = colStart
    seenSet.add((rowStart, colStart))
    keepRunning = True
    
    while(keepRunning):
        tempRow, tempCol = walk_forward(r, c, currentDirection, directions)
        if (0 <= tempRow < maxRow-1) and (0 <= tempCol < maxCol-1):
            if (tempRow, tempCol) in allowedSet:
                seenSet.add((tempRow, tempCol))
                r = tempRow
                c = tempCol
            else:
                currentDirection = turn_right(currentDirection)
        else:
            keepRunning = False
            break     

rowStart, colStart, allowedSet, seenSet, directions, currentDirection, maxRow, maxCol = get_data(day, year)
find_solution(rowStart, colStart, maxRow, maxCol, allowedSet, seenSet, currentDirection, directions)
print(f"Answer to Part 1: {len(seenSet)}")
