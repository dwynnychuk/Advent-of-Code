class Day01:
    def __init__(self):
        with open('2025/input_day01.txt') as f:
            self.data = f.read().splitlines()
            self.lower_limit = 0
            self.upper_limit = 99
            self.position = 50
            self.ends_at_num_count = 0
            self.num = 0
    
    def _check_limits_1(self) -> None:
        self.position = self.position % 100
        if self.position == self.num:
            self.ends_at_num_count += 1
    
    def _check_limits_2(self) -> None:
        if (self.position < self.lower_limit) or (self.position > self.upper_limit):
            self.ends_at_num_count += max((abs(self.position) // 100),1)
            self.position = self.position % 100
        
        if self.position == self.num:
            self.ends_at_num_count += 1
    
    def part1(self):
        for line in self.data:
            direction = line[0]
            magnitude = int(line[1:])
            if direction == "L":
                self.position -= magnitude
                self._check_limits_1()
            elif direction == "R":
                self.position += magnitude
                self._check_limits_1()
            else:
                raise ValueError("Invalid direction")
        print(f"The password is: {self.ends_at_num_count}")
            
    def part2(self):
        for line in self.data:
            direction = line[0]
            magnitude = int(line[1:])
            
            step = -1 if direction == "L" else 1
            for _ in range(magnitude):
                self.position = (self.position + step) % 100
                if self.position == self.num:
                    self.ends_at_num_count +=1
        print(f"The password is: {self.ends_at_num_count}")
    
if __name__ == "__main__":
    day01 = Day01()
    day01.part2()