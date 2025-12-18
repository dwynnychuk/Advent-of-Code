class Day03:
    def __init__(self):
        with open("2025/input_day03.txt") as f:
            self.data = f.read().splitlines()
            self.part2_cells = 12
            
    def solve_p1(self) -> None:
        total_output = 0
        for bank in self.data:
            total_output += self._get_max_joltage_dual(bank)
        print(f"The total output joltage for part one is: {total_output}")
    
    def solve_p2(self) -> None:
        total_output = 0
        for bank in self.data:
            total_output += self._get_max_joltage_n(bank, self.part2_cells)
        print(f"The total output joltage with {self.part2_cells} cells is: {total_output}")
    
    def _get_max_joltage_dual(self, bank: str) -> int:
        l = len(bank)
        max = int(bank[0:2])
        for idx1, i in enumerate(bank[0:-1:]):
            for j in bank[idx1+1::]:
                if int(str(i+j)) > max:
                    max = int(str(i+j))
        return max
    
    def _get_max_joltage_n(self, bank: str, num_cells: int) -> int:
        l = len(bank)
        joltage = []
        can_remove = l - num_cells
        
        for c in bank:
            while joltage and can_remove > 0 and joltage[-1] < c:
                joltage.pop()
                can_remove -= 1
            joltage.append(c)
        
        if len(joltage) > num_cells:
            joltage = joltage[:num_cells]
                  
        max = int("".join(joltage))                            
        return max
        
if __name__ == "__main__":
    problem = Day03()
    problem.solve_p1()
    problem.solve_p2()