import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()

passportList = []
currentPassport = []
for line in lines:
    if not len(line.strip()) == 0:
        currentPassport.append(line)
        if lines.index(line) == (len(lines) -1):
            passportList.append(currentPassport)
    else:
        passportList.append(currentPassport)
        currentPassport = []

passportStrings = []
for passport in passportList:
    passportItemstring = ''
    for item in passport:
        passportItemstring = passportItemstring + " " + item
    passportStrings.append(passportItemstring)


def isValidPassportPart1(passport, rules):
    items = passport.split()
    correctFields = 0
    for item in items:
        if item.split(":")[0] in rules:
            correctFields += 1
    return correctFields >= (len(rules)) 


def isValidPassportPart2(passport, rules):
    items = passport.split()
    correctFields = 0
    for item in items:
        if item.split(":")[0] in rules:
            key = item.split(":")[0]
            value = item.split(":")[1]
            if key == 'byr':
                correctFields += 1920 <= int(value) <= 2002
            elif key == "iyr":
                correctFields += 2010 <= int(value) <= 2020
            elif key == "eyr":
                correctFields += 2020 <= int(value) <= 2030
            elif key == "hgt":
                if value[-2:] == "cm":
                    correctFields += (150 <= float(value[:-2]) <= 193)
                elif value[-2:] =="in":
                    correctFields += (59 <= float(value[:-2]) <= 76)
            elif key == "hcl":
                correctFields += value[0] == "#" and len(value[1:]) == 6 and value[1:].isalnum()
            elif key == "ecl":
                try:
                    result = next((s for s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] if value in s))
                    correctFields +=  len(result) > 0
                except:
                    pass
            elif key == "pid":
                correctFields += len(value) == 9
    return correctFields >= (len(rules)) 


mustContain = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # Does not have to contain cid
amountOfValidPassportsPart1 = 0
for passport in passportStrings:
    if isValidPassportPart1(passport, mustContain):
        amountOfValidPassportsPart1 += 1

amountOfValidPassportsPart2 = 0
for passport in passportStrings:
    if isValidPassportPart2(passport, mustContain):
        amountOfValidPassportsPart2 += 1

print("Amount of valid passports part 1:", amountOfValidPassportsPart1)
print("Amount of valid passports part 2:", amountOfValidPassportsPart2)
