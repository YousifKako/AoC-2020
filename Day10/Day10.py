# First Puzzle
def solution_1():
    with open("Input.txt") as file:
        file_read = file.read()
    file_read_list = sorted(list(map(int, file_read.split("\n"))))
    diff_1 = 1
    diff_3 = 1
    for num in range(len(file_read_list)-1):
        diff = file_read_list[num+1] - file_read_list[num]
        if diff == 1:
            diff_1 += 1
        elif diff == 3:
            diff_3 += 1
    
    return diff_1 * diff_3

# Second Puzzle
def solution_2():
    pass


print(solution_1())
print(solution_2())