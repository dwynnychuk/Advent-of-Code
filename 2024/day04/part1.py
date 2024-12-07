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
    letter = Word(row, col)
    if (letter.check_up() == True) or (letter.check_down() == True) or (letter.check_left() == True) or (letter.check_right() == True) or (letter.check_diagonals() == True):
        print(f"row: {letter.y}, column: {letter.x}")

class Word:
    def __init__(self, row, column):
        self.x = column
        self.y = row
        
    def check_up(self) -> bool:
        if self.y < 3:
            return False
        else:
            if (data[self.y - 1][self.x] == "M") and (data[self.y - 2][self.x] == "A") and (data[self.y - 3][self.x] == "S"):
                return True 
            else:    
                return False
    
    def check_down(self) -> bool:
        if self.y > (sizeY - 3):
            return False
        else:
            if (data[self.y + 1][self.x] == "M") and (data[self.y + 2][self.x] == "A") and (data[self.y + 3][self.x] == "S"):
                return True
            else:
                return False
    
    def check_left(self) -> bool:
        if self.x < 3:
            return False
        else:
            if (data[self.y][self.x - 1] == "M") and (data[self.y][self.x - 2] == "A") and (data[self.y][self.x - 3] == "S"):
                return True
            else: 
                return False
    
    def check_right(self) -> bool:
        if self.x > (sizeX - 3):
            return False
        else:
            if (data[self.y][self.x + 1] == "M") and (data[self.y][self.x + 2] == "A") and (data[self.y][self.x + 3] == "S"):
                return 1
            else:
                return 0
    
    def check_diagonals(self) -> bool:
        pass
    

data , sizeX, sizeY = get_data(day, year)
search_input(data)

#val = Word(32,61)
#print(val.check_up())
#print(val.check_down())