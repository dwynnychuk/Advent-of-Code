class Day03:
    def __init__(self):
        with open("2025/input_day03.txt") as f:
            self.data = f.read().splitlines()
            
    def solve_p1(self) -> None:
        total_output = 0
        for bank in self.data:
            total_output += self._get_max_joltage(bank, 2)
        print(f"The total output joltage for part one is: {total_output}")
    
    def solve_p2(self) -> None:
        pass
    
    def _get_max_joltage(self, bank: str, num_batteries: int) -> int:
        l = len(bank)
        max = int(bank[0:num_batteries])
        for idx1, i in enumerate(bank[0:-1:]):
            for j in bank[idx1+1::]:
                if int(str(i+j)) > max:
                    max = int(str(i+j))
        return max
    
if __name__ == "__main__":
    problem = Day03()
    problem.solve_p1()
    problem.solve_p2()