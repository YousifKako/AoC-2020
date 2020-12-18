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
    dp = dict()
    def recurr(i):
        if i == len(file_read_list)-1:
            return 1
        if i in dp:
            return dp[i]
        ans = 0
        for j in range(i+1, len(file_read_list)):
            if file_read_list[j] - file_read_list[i] <= 3:
                ans += recurr(j)
        dp[i] = ans
        return ans

    with open("Input.txt") as file:
        file_read = file.read()
    file_read_list = list(map(int, file_read.split("\n")))
    file_read_list.append(0)
    file_read_list = sorted(file_read_list)
    file_read_list.append(max(file_read_list)+3)
    return recurr(0)


print(solution_1())
print(solution_2())