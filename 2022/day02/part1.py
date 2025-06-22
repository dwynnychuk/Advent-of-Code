# Day 02 of AOC 2022

with open("day02/input.txt") as f:
    data = f.read().splitlines()

def part01(data: list) -> int:
    total_score = 0
    for round in data:
        match round:
            case "A X":
                total_score += (1 + 3)
            case "A Y":
                total_score += (2 + 6)
            case "A Z":
                total_score += (3 + 0)
            case "B X":
                total_score += (1 + 0)
            case "B Y":
                total_score += (2 + 3)
            case "B Z":
                total_score += (3 + 6)
            case "C X":
                total_score += (1 + 6)
            case "C Y":
                total_score += (2 + 0)
            case "C Z":
                total_score += (3 + 3)
            
    return total_score
print(f"The solution to Part one is {part01(data)}")
    
        
