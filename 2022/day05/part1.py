#Day 05 of AOC2022

class Solution:
    def __init__(self, datafile):
        with open(datafile) as f:
            self.data = f.read().splitlines()
            
        self.stacks = {f"S{k}": [] for k in range(1,10,1)}
        for i in range(7,-1,-1):
            for j in range(1,10,1):
                if self.data[i][(j-1)*4+1] != " ":
                    self.stacks[f"S{j}"].append(self.data[i][(j-1)*4+1])

    def solvep1(self):
        output = []
        for move in self.data[10::]:
            _, num, _, fromstack, _, tostack = move.split(" ")
            self.move_item(int(num), int(fromstack), int(tostack))
        
        for val in self.stacks.values():
            output.append(val[-1])
        return output
                        
    def move_item(self, num, fromstack, tostack):
        for _ in range(num):
            temp = self.stacks[f"S{fromstack}"].pop()
            self.stacks[f"S{tostack}"].append(temp)

p1 = Solution("day05/input.txt")
print(f"Day 5 part 1 answer: {p1.solvep1()}")
        