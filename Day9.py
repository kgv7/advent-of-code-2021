def open_and_parse(filename):
    my_file = open(filename)
    i = 0
    parsed_list = []
    for line in my_file:
        stripped_line = list(line.rstrip())
        parsed_list.append(stripped_line)
        # i = i + 1
    return parsed_list

parsed_list = (open_and_parse('inputs-day9.txt'))
# print(len(parsed_list))
# print(len(parsed_list[0]))

# PART 1

def find_low_points(parsed_list):
# go through each row in list
    low_points = []
    for i in range(len(parsed_list)):
        #each element in that row
        for j in range(len(parsed_list[0])):
            element = int(parsed_list[i][j])
            min_ = element
            if element == 9:
                continue
            if (i-1) > -1:
                up = int(parsed_list[i-1][j])
                if up < min_:
                    min_ = up
            if (i + 1) < len(parsed_list):
                down = int(parsed_list[i+1][j])
                # min_ = min(min_, down)
                if down < min_:
                    min_ = down
            if (j - 1) > -1:
                left = int(parsed_list[i][j-1])
                # min_ = min(min_, left)
                if left < min_:
                    min_ = left
            if (j + 1) < len(parsed_list[0]):
                right = int(parsed_list[i][j+1])
                # min_ = min(min_, right)
                if right < min_:
                    min_ = right
            if min_ == element:
                low_points.append(element)

    return low_points

def part1_answer():
    low_points = find_low_points(parsed_list)
    
    sum_ = 0

    for point in low_points:
        sum_ += (point + 1)

    return sum_

print(part1_answer())


# PART 2

def part2_answer(parsed_list):

    low_points = find_low_points(parsed_list)
    
    # start looking at each number
    # look at each index of low_points
    # if # isn't the first index in low_points and isn't 9, add to the count
    # if it is the first number


    basin_size = []
    basin_count = 0
    for i in range(len(parsed_list)):
        #each element in that row
        for j in range(len(parsed_list[0])):
            pass
        pass

