def open_and_parse(filename):
    my_file = open(filename)
    i = 0
    parsed_list = []
    for line in my_file:
        stripped_line = list(line.rstrip())
        parsed_list.append(stripped_line)
        # i = i + 1
    return parsed_list

parsed_list = (open_and_parse('inputs-day10.txt'))

print(parsed_list)