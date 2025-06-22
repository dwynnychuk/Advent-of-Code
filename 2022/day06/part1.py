# AOC Day 6 2022
class Solution:
    def __init__(self, datafile):
        with open(datafile) as f:
            self.data = f.read()
    
    def solvep1(self):
        for i in range(3,len(self.data)):
            fourset = self.data[i-3:i+1]
            if len(fourset) == len(set(fourset)):
                return i + 1    # counter starts at 0

sol = Solution("day06/input.txt")
print(f"The first marker comes at index {sol.solvep1()}")