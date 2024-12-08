# AOC 2024 Day 04 Part 02
day = "04"
year = "2024"
global totalSum
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
            if data[row][col] == "A":
                run_checks(row, col)
                
def run_checks(row, col):
    global totalSum
    letter = Word(row, col)
    if (letter.check_mmss() == True) or (letter.check_msms() == True) or \
        (letter.check_smsm() == True) or (letter.check_ssmm() == True):
            totalSum += 1
        
class Word:
    def __init__(self, row, column):
        self.x = column
        self.y = row
        self.sizeX = sizeX
        self.sizeY = sizeY
    
    def check_mmss(self) -> bool:
        # m m
        #  a 
        # s s
        global totalSum
        if (self.x < 1) or (self.y < 1) or (self.x > self.sizeX - 2) or (self.y > self.sizeY - 2):
            return False
        elif (data[self.y - 1][self.x - 1] == "M") and (data[self.y - 1][self.x + 1] == "M") and \
            (data[self.y + 1][self.x - 1] == "S") and (data[self.y + 1][self.x + 1] == "S"):
            print(f"row: {self.y}, col: {self.x}. mmss")
            return True
        else:
            return False
    
    def check_msms(self) -> bool:
        # m s
        #  a 
        # m s
        global totalSum
        if (self.x < 1) or (self.y < 1) or (self.x > self.sizeX - 2) or (self.y > self.sizeY - 2):
            return False
        elif (data[self.y - 1][self.x - 1] == "M") and (data[self.y - 1][self.x + 1] == "S") and \
            (data[self.y + 1][self.x - 1] == "M") and (data[self.y + 1][self.x + 1] == "S"):
            print(f"row: {self.y}, col: {self.x}. msms")
            return True
        else:
            return False
        
    def check_smsm(self) -> bool:
        # s m
        #  a 
        # s m
        global totalSum
        if (self.x < 1) or (self.y < 1) or (self.x > self.sizeX - 2) or (self.y > self.sizeY - 2):
            return False
        elif (data[self.y - 1][self.x - 1] == "S") and (data[self.y - 1][self.x + 1] == "M") and \
            (data[self.y + 1][self.x - 1] == "S") and (data[self.y + 1][self.x + 1] == "M"):
            print(f"row: {self.y}, col: {self.x}. smsm")
            return True
        else:
            return False
        
    def check_ssmm(self) -> bool:
        # s s
        #  a 
        # m m
        global totalSum
        if (self.x < 1) or (self.y < 1) or (self.x > self.sizeX - 2) or (self.y > self.sizeY - 2):
            return False
        elif (data[self.y - 1][self.x - 1] == "S") and (data[self.y - 1][self.x + 1] == "S") and \
            (data[self.y + 1][self.x - 1] == "M") and (data[self.y + 1][self.x + 1] == "M"):
            print(f"row: {self.y}, col: {self.x}. ssmm")
            return True
        else:
            return False

    
data , sizeX, sizeY = get_data(day, year)
search_input(data)
print(f"The total sum is: {totalSum}")