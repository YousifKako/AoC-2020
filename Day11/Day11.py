# First Puzzle
def solution_1():
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    lamb = lambda x,y,i,j: (x+i, y+j)
    check = lambda x,y,x_len,y_len: (x>=0) and (x<=x_len) and (y>=0) and (y<=y_len)
    check_empty = lambda grid,x,y: grid[x][y] == 'L' or grid[x][y] == '.'
    check_occupied = lambda grid,x,y: grid[x][y] == '#'

    def foo(grid):
        to_return = list()
        x_len = len(grid) - 1
        y_len = len(grid[0]) - 1
        for i in range(len(grid)):
            string = ""
            for j in range(len(grid[i])):
                lst = [lamb(x,y,i,j) for x,y in directions]
                lst = [i for i in lst if check(i[0], i[1], x_len, y_len)]
                if grid[i][j] == '.':
                    string += '.'
                elif grid[i][j] == 'L':
                    empty = all(check_empty(grid, i[0], i[1]) for i in lst)
                    if empty:
                        string += '#'
                    else:
                        string += grid[i][j]
                else:
                    occupied = sum(check_occupied(grid, i[0], i[1]) for i in lst)
                    if occupied >= 4:
                        string += 'L'
                    else:
                        string += grid[i][j]
            to_return.append(string)
        return to_return

    with open("Input.txt") as file:
        file_read = file.read().split("\n")

    prev_grid = file_read
    while True:
        new_grid = foo(prev_grid)
        if prev_grid == new_grid:
            break
        prev_grid = new_grid
    count = 0
    for i in prev_grid:
        for j in i:
            if j == '#':
                count += 1
    return count

# Second Puzzle
def solution_2():
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    def check(grid, i, j, check):
        count = 0
        storage = [i, j]
        for d in directions:
            i, j = storage
            while True:
                i, j = i-d[0], j-d[1]
                if (i >= 0) and (j >= 0) and (i <= len(grid)-1) and (j <= len(grid[0])-1):
                    symbol = grid[i][j]
                    if symbol == '#':
                        if check == '#':
                            if count >= 5:
                                return count
                            count += 1
                            break
                        else:
                            return False
                    elif symbol == 'L':
                        break
                else:
                    break

        return count if check == '#' else True

    def bar(grid):
        to_return = list()
        for i in range(len(grid)):
            string = ""
            for j in range(len(grid[i])):
                if grid[i][j] == '.':
                    string += '.'
                elif grid[i][j] == 'L':
                    empty = check(grid, i, j, 'L')
                    if empty:
                        string += '#'
                    else:
                        string += grid[i][j]
                else:
                    occupied = check(grid, i, j, '#')
                    if occupied >= 5:
                        string += 'L'
                    else:
                        string += grid[i][j]
            to_return.append(string)
        return to_return

    with open("Input.txt") as file:
        file_read = file.read().split("\n")

    prev_grid = file_read
    while True:
        new_grid = bar(prev_grid)
        if prev_grid == new_grid:
            break
        prev_grid = new_grid
    count = 0
    for i in prev_grid:
        for j in i:
            if j == '#':
                count += 1
    return count

print(solution_1())
print(solution_2())