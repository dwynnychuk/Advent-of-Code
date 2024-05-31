# AOC 2020 day 4
with open("day04/input.txt") as file:
    data = file.read().split('\n\n')

requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
byrLim = [1920, 2002]
iyrLim = [2010, 2020]
eyrLim = [2020, 2030]
hgtInLim = [59, 76]
hgtCmLim = [150, 193]
hclLim = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
eclLim = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
pidLim = 9

def checkByr(byr):
    if (int(byr) >= byrLim[0]) and (int(byr) <= byrLim[1]):
        return True
    else:
        return False

def checkIyr(iyr):
    if (int(iyr) >= iyrLim[0]) and (int(iyr) <= iyrLim[1]):
        return True
    else:
        return False
    
def checkEyr(eyr):
    if (int(eyr) >= eyrLim[0]) and (int(eyr) <= eyrLim[1]):
        return True
    else:
        return False

def checkHgt(hgt):
    if hgt.endswith('in'):
        hgtCheck = hgtInLim
    elif hgt.endswith('cm'):
        hgtCheck = hgtCmLim
    else:
        return False

    if (int(hgt[:-2]) >= hgtCheck[0]) and (int(hgt[:-2]) <= hgtCheck[1]):
        return True
    else:
        return False

def checkHcl(hcl):
    if ord(hcl[0]) == 35:
        if len(hcl) == 7:
            for idx in hcl[1:]:
                if idx not in hclLim:
                    return False
            return True

def checkEcl(ecl):
    if ecl in eclLim:
        return True
    else:
        return False
    
def checkPid(pid):
    if (len(pid) == pidLim) and (pid.isnumeric()):
        return True
    else:
        return False

sumValid1 = 0
sumValid2 = 0

# Part 1
for line in data:
    line = line.replace('\n', ' ')
    fields = line.split(' ')
    keys = []
    for field in fields:
        separatedFields = field.split(':')
        keys.append(separatedFields[0])
    valid = all([item in keys for item in requiredFields])
    sumValid1 += valid

# Part 2
for line in data:
    line = line.replace('\n',' ')
    fields = line.split(' ')
    fieldDict = dict()
    for field in fields:
        separatedFields = field.split(':')
        fieldDict[separatedFields[0]] = separatedFields[1]
    valid = all([item in fieldDict.keys() for item in requiredFields])
    
    if valid:
        # Check for Pt Solution
        validByr = checkByr(fieldDict['byr'])
        validIyr = checkIyr(fieldDict['iyr'])
        validEyr = checkEyr(fieldDict['eyr'])
        validHgt = checkHgt(fieldDict['hgt'])
        validHcl = checkHcl(fieldDict['hcl'])
        validEcl = checkEcl(fieldDict['ecl'])
        validPid = checkPid(fieldDict['pid'])

        if validIyr and validEyr and validByr and validHgt and validHcl and validEcl and validPid:
            sumValid2 += 1

print("The solution to part 1 is: " + str(sumValid1) + "!")
print("The solution to part 2 is: " + str(sumValid2) + "!")





    