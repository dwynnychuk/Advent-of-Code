class Day02:
    def __init__(self):
        with open("2025/input_day02.txt") as f:
            self.data = f.read().split(',')
        
        
    def solve_p1(self) -> None:
        invalid_sum = 0
        for ids in self.data:
            id1, id2 = ids.split("-")

            for val in range(int(id1),int(id2)+1):
                l = len(str(val))
                if (l % 2) == 1:
                    continue
                elif str(val)[0:int(l/2)] == str(val)[int(l/2):]:
                    invalid_sum += val            
        print(f"Total invalid sum for part 1 is: {invalid_sum}")
        
    def solve_p2(self) -> None:
        invalid_sum = 0
        
        for ids in self.data:
            id1, id2 = ids.split("-")
            
            for val in range(int(id1), int(id2)+1):
                # business logic here
                s = str(val)
                l = len(s)
                if l > 1:
                    for i in range(2, l+1):
                        if (l % i) == 0:
                            # if this value is divisible by value
                            c = l // i
                            cs = []
                            for j in range(l//c):
                                start = j*c
                                end = start + c
                                cs.append(s[start:end])
                            if len(set(cs)) == 1:
                                invalid_sum += val
                                break
        
        print(f"The sum of all invalid ID's for part two is: {invalid_sum}")
        
if __name__ == "__main__":
    problem = Day02()
    problem.solve_p1()
    problem.solve_p2()
    
        