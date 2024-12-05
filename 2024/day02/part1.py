# AOC 2024 Day 02 Part 01
day = "02"
year = "2024"

def get_data(day, year):
    with open(year + "/day" + day + "/input.txt") as file:
        data = file.read().splitlines()
    return data

def scrub_data(data):
    safeValues = 0
    for line in data:
        values = make_list(line)
        safeValues = safeValues + check_if_safe(values)
        print(f"{values} and {safeValues}")
    return safeValues

def make_list(line):
    values = list(map(int, line.split(" ")))
    return values

def check_if_safe(values) -> int:
    
    if abs(values[1] - values[0]) > 3:
        # first value violates big jump rule
        # print("Big Jump")
        return 0
    
    elif (values[1] > values[0]):
        # increasing and no initial big jump
        for idx in range(1,len(values)):
            if (values[idx] > values[idx-1]) and (abs(values[idx] - values[idx-1]) <= 3):
                if (idx == (len(values)-1)):
                    #print(f"Safe increasing: {values}")
                    return 1
                else:
                    continue
            else:
                return 0
            
    elif (values[1] < values[0]):
        # decreasing and no initial big jump
        for idx in range(1,len(values)):
            if (values[idx] < values[idx-1]) and (abs(values[idx] - values[idx-1]) <= 3):
                if (idx == (len(values)-1)):
                    #print(f"Safe decreasing: {values}")
                    return 1
                else:
                    continue
            else:
                return 0
    elif (values[1] == values[0]):
        del values[0]
        # return check_if_safe(values)
        return 0
    else:
        print("ERROR")
        return 0

answer = scrub_data(get_data(day, year))
print(answer)
