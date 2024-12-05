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


# def check_if_safe(values, first) -> int:
    
#     if (values[1] > values[0]):
#         # increasing and no initial big jump
#         for idx in range(1,len(values)):
#             if (values[idx] > values[idx-1]) and (abs(values[idx] - values[idx-1]) <= 3):
#                 if (idx == (len(values)-1)):
#                     return 1
#                 elif ((idx == 1) and not ((values[idx+1] > values[idx]) and (abs(values[idx+1] - values[idx]) <= 3)) and first == True):
#                     values0 = values[:]
#                     del values0[idx-1]
#                     return check_if_safe(values0, False)
#                 else:
#                     continue
#             else:
#                 if first == True:
#                     values0 = values[:]
#                     values1 = values[:]
#                     del values0[idx-1]
#                     del values1[idx]
#                     return max(check_if_safe(values0, False), check_if_safe(values1, False))
#                 else:
#                     return 0
            
#     elif (values[1] < values[0]):
#         # decreasing and no initial big jump
#         for idx in range(1,len(values)):
#             if (values[idx] < values[idx-1]) and (abs(values[idx] - values[idx-1]) <= 3):
#                 if (idx == (len(values)-1)):
#                     #print(f"Safe decreasing: {values}")
#                     return 1
#                 elif ((idx == 1) and not ((values[idx+1] < values[idx]) and (abs(values[idx+1] - values[idx]) <= 3)) and first == True):
#                     values0 = values[:]
#                     del values0[idx-1]
#                     return check_if_safe(values0, False)
#                 else:
#                     continue
#             else:
#                 if first == True:
#                     values0 = values[:]
#                     values1 = values[:]
#                     del values0[idx-1]
#                     del values1[idx]
#                     return max(check_if_safe(values0, False), check_if_safe(values1, False))
#                 else:
#                     return 0
            
#     elif (values[1] == values[0]):
#         if first == True:
#             del values[0]
#             return check_if_safe(values, False)
#         else:
#             return 0
    
#     else:
#         print("ERROR")
#         return 0
