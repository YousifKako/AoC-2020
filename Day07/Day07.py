import re

# First Puzzle
def solution_1():
    with open("Input.txt") as file:
        di = dict()
        for line in file:
            line = re.split(" bag | bags | bag, | bags, | bag.\n| bags.\n|contain ", line)[:-1]
            del line[1]
            di[line[0]] = [i[2:] if i[0] in ['1','2','3','4','5','6','7','8','9'] else i for i in line]

        set_count, start = set(), 0
        while True:
            for k in di.keys():
                for v in di[k]:
                    if v in set_count or v == "shiny gold":
                        set_count.add(k)
            if len(set_count) > start:
                start = len(set_count)
            else:
                break
        return start-1

# Second Puzzle
def solution_2():
    with open("Input.txt") as file:
        di = dict()
        for line in file:
            line = re.split(" bag | bags | bag, | bags, | bag.\n| bags.\n|contain ", line)[:-1]
            del line[1]
            di[line[0]] = line[1:]

    def recurr(bag):
        count = 1
        for i in di[bag]:
            try:
                count += int(i[0])*recurr(i[2:])
            except:
                continue
        return count
    return recurr("shiny gold") - 1


print(solution_1())
print(solution_2())