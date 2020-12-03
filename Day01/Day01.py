# First Puzzle
def two_sum(lst, target):
    st = set()
    for i in lst:
        temp = target - i
        if temp in st:
            print("{} + {} = {} | {} * {} = {}".format(temp, i, temp+i, temp, i, temp*i))
        st.add(i)

# Second Puzzle
def three_sum(lst, target):
    for i in range(len(lst)-1):
        st = set()
        temp = target - lst[i]
        for j in range(i + 1, len(lst)):
            temp_2 = temp - lst[j]
            if temp_2 in st:
                print("{} + {} + {} = {} | {} * {} * {} = {}".format(temp_2, lst[i], lst[j], temp_2+lst[i]+lst[j], temp_2, lst[i], lst[j], temp_2*lst[i]*lst[j]))
            st.add(lst[j])


with open("Input.txt") as file:
    lst = [int(sub) for sub in file]
    two_sum(lst, 2020)
    three_sum(lst, 2020)