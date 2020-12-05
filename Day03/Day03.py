# First Puzzle
def solution_1(x, y):
    with open("Input.txt") as file:
        file_read = file.read()
    height = file_read.count('\n')
    width = 31
    file_read = file_read.split('\n')
    x_count = x
    tree_count = 0
    for i in range(y, len(file_read), y):
        if x_count % x == 0:
            height -= 1
            if file_read[i][x_count % width] == '#':
                tree_count += 1
        x_count += x
    return tree_count

# Second Puzzle
def solution_2():
    slope_1 = solution_1(1, 1)
    slope_2 = solution_1(3, 1)
    slope_3 = solution_1(5, 1)
    slope_4 = solution_1(7, 1)
    slope_5 = solution_1(1, 2)
    return slope_1 * slope_2 * slope_3 * slope_4 * slope_5


print(solution_1(3, 1))
print(solution_2())