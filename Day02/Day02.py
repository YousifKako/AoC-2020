import re

# First Puzzle
def solution_1():
    with open("Input.txt") as file:
        count = 0
        for i in file:
            st = re.split('-| +|:|\n', i)
            temp = st[4].count(st[2])
            if temp >= int(st[0]) and temp <= int(st[1]):
                count += 1
        print(count)

# First Puzzle
def solution_2():
    with open("Input.txt") as file:
        count = 0
        for i in file:
            st = re.split('-| +|:|\n', i)
            temp_1 = st[4][int(st[0])-1]
            temp_2 = st[4][int(st[1])-1]
            if (temp_1 == st[2] and temp_2 != st[2]) or (temp_2 == st[2] and temp_1 != st[2]):
                count += 1
        print(count)


solution_1()
solution_2()
