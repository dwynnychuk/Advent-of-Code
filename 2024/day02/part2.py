# AOC 2024 Day 02 Part 02
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
        isLineInitiallySafe = check_if_safe(values)
        if isLineInitiallySafe == 1:
            safeValues += 1
        else:
            tempSafe = 0
            for dvar in range(len(values)):
                tempValues = values[:]
                del tempValues[dvar]
                print(tempValues)
                tempSafe = tempSafe + check_if_safe(tempValues)
            if tempSafe > 0:
                safeValues += 1
                
    return safeValues

def make_list(line):
    values = list(map(int, line.split(" ")))
    return values

def check_if_safe(values) -> int:
    if (values[1] > values[0]):
        for idx in range(1,len(values)):
            if (values[idx] > values[idx-1]) and (abs(values[idx] - values[idx-1]) <= 3):
                if (idx == (len(values)-1)):
                    return 1
                else:
                    continue
            else:
                return 0
            
    elif (values[1] < values[0]):
        for idx in range(1,len(values)):
            if (values[idx] < values[idx-1]) and (abs(values[idx] - values[idx-1]) <= 3):
                if (idx == (len(values)-1)):
                    return 1
                else:
                    continue
            else:
                return 0
    else:
        return 0

answer = scrub_data(get_data(day, year))
print(answer)