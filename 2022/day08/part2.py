# AOC 2022 day 8
import numpy as np

class Solution:
    def __init__(self, filepath):
        with open(filepath) as f:
            self.d = f.read().splitlines()
        
        self.scenic = np.zeros([len(self.d), len(self.d[0])], dtype=int)
        self.data = np.zeros_like(self.scenic)
        
    def part02(self) -> int:
        for r in range(len(self.d)):
            for c in range(len(self.d[0])):
                self.data[r][c] = int(self.d[r][c])
        for r in range(1,len(self.data)-1):     # all exterior will see 0 * something
            for c in range(1,len(self.data[0])-1):        
                self.scenic[r,c] = self.check_scenic(r,c)
        return np.max(np.max(self.scenic))
                    
    def check_scenic(self, row, column) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]   #up, down, left, right
        multvec = []
        tempscore = 1
        for d in dirs:
            dr , dc = d
            counter = 0
            while True:
                counter += 1
                newrow, newcol = row + counter*dr, column + counter*dc
                if newrow < 0 or newrow > self.data.shape[0]-1 or newcol < 0 or newcol > self.data.shape[1]-1:
                    counter -= 1
                    break
                
                if self.data[newrow, newcol] >= self.data[row,column]:
                    break
            multvec.append(counter)
        for m in multvec:
            tempscore = tempscore * m
        return tempscore

sol = Solution("day08/input.txt")
print(f"The maximum scenic score is {sol.part02()}")