# First Puzzle
def solution_1():
    with open("Input.txt") as file:
        file_read = file.read()
    file_read_list = file_read.split("\n")
    file_length = len(file_read_list)
    count_list = [0] * file_length
    i, accumulator = 0, 0
    while i < file_length:
        line = file_read_list[i].split(" ")
        if count_list[i] == 1:
            break
        if line[0] == 'acc':
            accumulator += int(line[1])
        elif line[0] == 'jmp':
            i += int(line[1])
            continue
        count_list[i] = 1
        i += 1
    return accumulator
    

# Second Puzzle
def solution_2():
    pass


print(solution_1())
print(solution_2())