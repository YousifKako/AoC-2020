from itertools import product

# First Puzzle
def solution_1():
    def get_previous(lst, number):
        lst = lst[len(lst)-number:]
        return [x+y for x,y in product(lst, lst)]

    with open("Input.txt") as file:
        file_read = file.read()
    file_read_list = list(map(int, file_read.split("\n")))
    for i in range(25, len(file_read_list)):
        previous_sum_list = get_previous(file_read_list[:i], 25)
        if file_read_list[i] not in previous_sum_list:
            return file_read_list[i], file_read_list[len(file_read_list)-i:i]

# Second Puzzle
def solution_2(number, lst):
    for i in range(len(lst)-1):
        total_sum = lst[i]
        for j in range(i+1, len(lst)):
            if total_sum == number:
                final = sorted(lst[i:j])
                return final[0] + final[len(final)-1]
            elif total_sum > number:
                break
            total_sum += lst[j]


number, lst = solution_1()
print(number)
print(solution_2(number, lst))