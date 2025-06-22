# Day 03 of AOC 2022

class Solution:
    def __init__(self, datafile):
        with open(datafile) as f:
            self.data = f.read().splitlines()
        self.total_priority = 0
        self.priority = {"a": 1,
                         "b": 2,
                         "c": 3,
                         "d": 4,
                         "e": 5,
                         "f": 6,
                         "g": 7,
                         "h": 8,
                         "i": 9,
                         "j": 10,
                         "k": 11,
                         "l": 12,
                         "m": 13,
                         "n": 14,
                         "o": 15,
                         "p": 16,
                         "q": 17,
                         "r": 18,
                         "s": 19,
                         "t": 20,
                         "u": 21,
                         "v": 22,
                         "w": 23,
                         "y": 24,
                         "x": 25,
                         "z": 26,
                         "A": 27,
                         "B": 28,
                         "C": 29,
                         "D": 30,
                         "E": 31,
                         "F": 32,
                         "G": 33,
                         "H": 34,
                         "I": 35,
                         "J": 36,
                         "K": 37,
                         "L": 38,
                         "M": 39,
                         "N": 40,
                         "O": 41,
                         "P": 42,
                         "Q": 43,
                         "R": 44,
                         "S": 45,
                         "T": 46,
                         "U": 47,
                         "V": 48,
                         "W": 49,
                         "X": 50,
                         "Y": 51,
                         "Z": 52}
    
    def calculate_priority(self, item: str) -> int:
        return self.priority[item]
        
    def solvep1(self) -> int:
        for sack in self.data:
            self.s1 = sack[0:int(len(sack)/2)]
            self.s2 = sack[int(len(sack)/2):]
            for item in self.s1:
                if item in self.s2:
                    self.total_priority += self.calculate_priority(item)
                    break
        return self.total_priority
            
problem = Solution("day03/input.txt")
print(f"The solution is: {problem.solvep1()}")