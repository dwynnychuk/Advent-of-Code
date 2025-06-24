# AOC 2022 day 8
import numpy as np

class Solution:
    def __init__(self, filepath):
        with open(filepath) as f:
            self.d = f.read().splitlines()
        
        self.visible = np.zeros([len(self.d), len(self.d[0])], dtype=int)
        self.data = np.zeros_like(self.visible)
        self.visible[0,:] = 1
        self.visible[-1,:] = 1
        self.visible[:,0] = 1
        self.visible[:,-1] = 1
        
    def part01(self) -> int:
        for r in range(len(self.d)):
            for c in range(len(self.d[0])):
                self.data[r][c] = int(self.d[r][c])
        for r in range(len(self.data)):
            for c in range(len(self.data[0])):        
                if self.visible[r,c] != 1:
                    self.visible[r,c] = self.check_height(r,c)
        return np.sum(self.visible, axis=None)
                    
    def check_height(self, row, column) -> int:
        if np.all(self.data[row][0:column] < self.data[row][column]):
            return 1
        elif np.all(self.data[row,column+1:] < self.data[row][column]):
            return 1
        elif np.all(self.data[0:row,column] < self.data[row][column]):
            return 1
        elif np.all(self.data[row+1:,column] < self.data[row][column]):
            return 1
        else:
            return 0

sol = Solution("day08/input.txt")
print(f"The sume of visible trees is {sol.part01()}")
