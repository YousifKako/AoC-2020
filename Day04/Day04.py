import re

# First Puzzle
def solution_1():
    with open("Input.txt") as file:
        file_read = file.read()
    lst = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    file_read = file_read.split("\n\n")
    valid_count = 0
    count = 0
    to_return = list()
    for i in file_read:
        for j in lst:
            if j in i:
                count += 1
        if count == len(lst):
            to_return.append(i)
            valid_count += 1
        count = 0
    return valid_count, to_return

# second Puzzle
def solution_2(solution_one_list):
    ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    letters = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'w', 'z']
    valid_count = 0
    for i in solution_one_list:
        count = 0
        i = re.split("\n| ", i)
        for j in i:
            value = j.split(':')
            if value[0] == 'byr' and int(value[1]) >= 1920 and int(value[1]) <= 2002:
                count += 1
            elif value[0] == 'iyr' and int(value[1]) >= 2010 and int(value[1]) <= 2020:
                count += 1
            elif value[0] == 'eyr' and int(value[1]) >= 2020 and int(value[1]) <= 2030:
                count += 1
            elif value[0] == 'hgt':
                if 'cm' in value[1]:
                    num = int(value[1].replace('cm', ''))
                    if num >= 150 and num <= 193:
                        count += 1
                elif 'in' in value[1]:
                    num = int(value[1].replace('in', ''))
                    if num >= 59 and num <= 76:
                        count += 1
            elif value[0] == 'hcl' and len(value[1][1:]) == 6:
                validation = 0
                for k in letters:
                    if k in value[1][1:]:
                        validation += 1
                        break
                if validation == 0:
                    count += 1
            elif value[0] == 'ecl' and len(value[1]) == 3:
                for k in ecl_list:
                    if value[1] == k:
                        count += 1
                        break
            elif value[0] == 'pid' and len(value[1]) == 9:
                count += 1
        if count == 7:
            valid_count += 1

    return valid_count


valid_count, returned_list = solution_1()
print(valid_count)
print(solution_2(returned_list))