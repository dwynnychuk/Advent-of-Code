class Day02:
    def __init__(self):
        with open("2025/input_day02.txt") as f:
            self.data = f.read().split(',')
        self.invalid_sum = 0
        
    def solve_p1(self):
        for ids in self.data:
            id1, id2 = ids.split("-")

            for val in range(int(id1),int(id2)+1):
                l = len(str(val))
                if (l % 2) == 1:
                    continue
                elif str(val)[0:int(l/2)] == str(val)[int(l/2):]:
                    self.invalid_sum += val            
        print(f"Total invalid sum for part 1 is: {self.invalid_sum}")
        
if __name__ == "__main__":
    problem = Day02()
    problem.solve_p1()
    
        