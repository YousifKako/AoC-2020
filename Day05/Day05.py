import math

# First Puzzle
def solution_1():
    lst = list()
    with open("Input.txt") as file:
        for line in file:
            line = line.replace('\n', '')
            num_F = 127
            num_B = 0
            num_R = 7
            num_L = 0
            for i in line:
                if i == 'F':
                    num_F = math.floor((num_F + num_B) / 2)
                elif i == 'B':
                    num_B = math.ceil((num_F + num_B) / 2)
                elif i == 'R':
                    num_L = math.ceil((num_L + num_R) / 2)
                elif i == 'L':
                    num_R = math.floor((num_L + num_R) / 2)
            lst.append((num_B * 8) + num_R)
        return sorted(lst)

# Second Puzzle
def solution_2(lst):
    for i in range(len(lst)-1):
        if lst[i]+1 != lst[i+1]:
            return lst[i] + 1


lst = solution_1()
print(max(lst))
print(solution_2(lst))