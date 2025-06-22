# Day 04 of AOC 2022
import numpy as np
class Solution():
    def __init__(self, datafile):
        with open(datafile) as f:
            self.data = f.read().splitlines()
        self.total_contain = 0
        
    def part02(self) -> int:
        for pair in self.data:
            r1t, r2t = pair.split(",")
            r1l, r1h = r1t.split("-")
            r2l, r2h = r2t.split("-")
            arr = np.array([r1l, r1h, r2l, r2h], dtype = int)
            self.total_contain += self.check_if_contained(arr)
        return self.total_contain

    def check_if_contained(self, arr: list) -> int:
        if arr[0] <= arr[2] and arr[1] >= arr[3]:
            return 1
        elif arr[2] <= arr[0] and arr[3] >= arr[1]:
            return 1
        elif arr[0] <= arr[2] and arr[1] >= arr[2]:
            return 1
        elif arr[2] <= arr[0] and arr[3] >= arr[0]:
            return 1
        else:
            return 0
        
p1 = Solution("day04/input.txt")
print(f"Solution to day 04 part 2 is: {p1.part02()}") 