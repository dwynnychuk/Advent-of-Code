# AOC day 7 2022

class Problem:
    def __init__(self, filepath):
        with open(filepath) as f:
            self.data = f.read().splitlines()
        self.current_path = ""
        self.directories = dict()
        self.folders = ["/"]
        self.totalsum = 0
        self.threshold = 100000
        
    def solvep1(self):
        for line in self.data:
            self.parse_line(line)
        for val in self.directories.values():
            if val <= self.threshold:
                self.totalsum += val
    
    def parse_line(self, line: str):
        if line.startswith("$ cd /"):
            self.current_path = "/"
            self.folders = ["/"]
            self.add_folder(self.current_path)
            
        elif line.startswith("$ cd .."):
            self.current_path = "/".join(self.current_path.split("/")[:-1])
            self.folders.pop()
            
        elif line.startswith("$ cd"):
            if len(self.folders) == 1:
                self.current_path += line.split(" ")[-1]
            else:
                self.current_path += "/" + line.split(" ")[-1]
            self.folders.append(self.current_path)
            self.add_folder(self.current_path) 
            
        elif line[0].isdigit():
            fs = int(line.split(" ")[0])
            for dir in self.folders:
                self.directories[dir] += fs
            
    def add_folder(self, path: str) -> None:
        if path not in self.directories.keys():
            self.directories[path] = 0

prob = Problem("day07/input.txt")
sol = prob.solvep1()
print(f"The total sum is: {prob.totalsum}")
        