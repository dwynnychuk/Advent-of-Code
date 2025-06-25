# AOC 2022 day 09
import numpy as np

class Solution:
    def __init__(self, filepath):
        with open(filepath) as f:
            self.data = f.read().splitlines()
            self.hpos = [0,0]
            self.tpos = [0,0]
            self.dirs = {"U": (-1,0),
                         "D": (1,0),
                         "L": (0,-1),
                         "R": (0,1)}
            self.t_history = set()
            self.current_dir = []
            self.last_dir = []
        
    def solvep1(self) -> int:
        for line in self.data:
            direction, moves = line.split(" ")
            self.update_positions(direction,int(moves))
            self.t_history.add((self.tpos[0], self.tpos[1]))
        return len(self.t_history)
            
    def update_positions(self, directions, moves):
        self.current_dir = list(self.dirs[directions])

        for _ in range(moves):            
            # updating head position
            self.hpos[0], self.hpos[1] = self.hpos[0] + self.current_dir[0], self.hpos[1] + self.current_dir[1]
            maxdif = np.max([np.abs(self.hpos[0] - self.tpos[0]),np.abs(self.hpos[1] - self.tpos[1])])
            #print(self.hpos, self.tpos, directions,moves, maxdif)                 
            if maxdif > 1:
                if np.min((np.abs(self.hpos[0] - self.tpos[0]),np.abs(self.hpos[1] - self.tpos[1]))) == 0:
                    self.tpos[0], self.tpos[1] = self.tpos[0] + self.current_dir[0], self.tpos[1] + self.current_dir[1]
                else:
                    #diagonal
                    dy = -1 if self.hpos[0] - self.tpos[0] < 0 else 1
                    dx = -1 if self.hpos[1] - self.tpos[1] < 0 else 1
                        
                    self.tpos[0], self.tpos[1] = self.tpos[0] + dy, self.tpos[1] + dx   
            else:
                continue   
            
            print(self.hpos, self.tpos, directions,moves)                 

day09 = Solution("day09/input.txt")
print(f"The number of unique positions for the tail is: {day09.solvep1()}")