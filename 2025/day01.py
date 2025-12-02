class Day01:
    def __init__(self):
        with open('2025/input_day01.txt') as f:
            self.data = f.read().splitlines()
            self.lower_limit = 0
            self.upper_limit = 99
            self.position = 50
            self.ends_at_num_count = 0
            self.num = 0
    
    def _check_limits(self) -> None:
        print(self.position)
        self.position = self.position % 100
        if self.position == self.num:
            self.ends_at_num_count += 1
        print(self.position)
        print("\n")
    
    def part1(self):
        for line in self.data:
            direction = line[0]
            magnitude = int(line[1:])
            if direction == "L":
                self.position -= magnitude
                self._check_limits()
            elif direction == "R":
                self.position += magnitude
                self._check_limits()
            else:
                raise ValueError("Invalid direction")
        print(f"The password is: {self.ends_at_num_count}")
            
    def part2(self):
        pass
    
    
if __name__ == "__main__":
    day01 = Day01()
    day01.part1()