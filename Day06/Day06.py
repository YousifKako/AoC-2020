import string

# First Puzzle
def solution_1():
    with open("Input.txt") as file:
        read_file = file.read()
    read_file = read_file.split("\n\n")
    total_sum = 0
    for i in read_file:
        lines = i.split("\n")
        letters = dict.fromkeys(string.ascii_lowercase, 1)
        for line in lines:
            for char in line:
                if letters[char] == 1:
                    letters[char] = 0
                    total_sum += 1
    return total_sum

# Second Puzzle
def solution_2():
    with open("Input.txt") as file:
        read_file = file.read()
    read_file = read_file.split("\n\n")
    total_sum = 0
    for i in read_file:
        lines = i.split("\n")
        num_lines = len(lines)
        letters = dict.fromkeys(string.ascii_lowercase, num_lines)
        num_lines -= 1
        for line in lines:
            for char in line:
                if letters[char] == num_lines + 1:
                    letters[char] = num_lines

            num_lines -= 1
        for letter in letters:
            if letters[letter] == 0:
                total_sum += 1
    return total_sum


print(solution_1())
print(solution_2())