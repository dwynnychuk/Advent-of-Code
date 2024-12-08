# AOC 2024 Day 04 Part 01
day = "04"
year = "2024"
global sizeX, sizeY, totalSum
sizeX = 0
sizeY = 0
totalSum = 0


def get_data(day, year):
    with open(year + "/day" + day + "/input.txt") as file:
        data = file.read().splitlines()
    sizeX = len(data[0])
    sizeY = len(data)
    return data, sizeX, sizeY

def search_input(data):
    for row in range(sizeY):
        for col in range(sizeX):
            if data[row][col] == "X":
                run_checks(row, col)
                
def run_checks(row, col):
    global totalSum
    letter = Word(row, col)
    letter.check_up()
    letter.check_down()
    letter.check_left()
    letter.check_right()
    letter.check_diagonal_NW()
    letter.check_diagonal_NE()
    letter.check_diagonal_SW()
    letter.check_diagonal_SE()
        
class Word:
    def __init__(self, row, column):
        self.x = column
        self.y = row
        
    def check_up(self) -> bool:
        global totalSum
        if self.y < 3:
            return False
        else:
            if (data[self.y - 1][self.x] == "M") and (data[self.y - 2][self.x] == "A") and (data[self.y - 3][self.x] == "S"):
                totalSum += 1
                return True 
            else:    
                return False
    
    def check_down(self) -> bool:
        global totalSum
        if self.y > (sizeY - 4):
            return False
        else:
            if (data[self.y + 1][self.x] == "M") and (data[self.y + 2][self.x] == "A") and (data[self.y + 3][self.x] == "S"):
                totalSum += 1
                return True
            else:
                return False
    
    def check_left(self) -> bool:
        global totalSum
        if self.x < 3:
            return False
        else:
            if (data[self.y][self.x - 1] == "M") and (data[self.y][self.x - 2] == "A") and (data[self.y][self.x - 3] == "S"):
                totalSum += 1
                return True
            else: 
                return False
    
    def check_right(self) -> bool:
        global totalSum
        if self.x > (sizeX - 4):
            return False
        else:
            if (data[self.y][self.x + 1] == "M") and (data[self.y][self.x + 2] == "A") and (data[self.y][self.x + 3] == "S"):
                totalSum += 1
                return True
            else:
                return False
    
    def check_diagonal_NW(self) -> bool:
        global totalSum
        if (self.x < 3) or (self.y < 3):
            return False
        elif (data[self.y - 1][self.x - 1] == "M") and (data[self.y - 2][self.x - 2] == "A") and (data[self.y - 3][self.x - 3] == "S"):
            totalSum += 1
            return True
        else:
            return False
    
    def check_diagonal_NE(self) -> bool:
        global totalSum
        if (self.x > sizeX - 4) or (self.y < 3):
            return False
        elif (data[self.y - 1][self.x + 1] == "M") and (data[self.y - 2][self.x + 2] == "A") and (data[self.y - 3][self.x + 3] == "S"):
            totalSum += 1
            return True
        else:
            return False
    
    def check_diagonal_SW(self) -> bool:
        global totalSum
        if (self.x < 3) or (self.y > sizeY - 4):
            return False
        elif (data[self.y + 1][self.x - 1] == "M") and (data[self.y + 2][self.x - 2] == "A") and (data[self.y + 3][self.x - 3] == "S"):
            totalSum += 1
            return True
        else:
            return False
    
    def check_diagonal_SE(self) -> bool:
        global totalSum
        if (self.x > sizeX - 4) or (self.y > sizeY - 4):
            return False
        elif (data[self.y + 1][self.x + 1] == "M") and (data[self.y + 2][self.x + 2] == "A") and (data[self.y + 3][self.x + 3] == "S"):
            totalSum += 1
            return True
        else:
            return False
    
data , sizeX, sizeY = get_data(day, year)
search_input(data)
print(f"The total sum is: {totalSum}")