def open_file():
    """Create list of inputs for Day 2 Advent of Code."""

    file = open("inputs-day2.csv")

    inputs = []

    for line in file:
        line = line.rstrip()
        direction, num = line.split(" ")
        num = int(num)
        inputs.append((direction, num))

    return inputs


# Now, you need to figure out how to pilot this thing.

# It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.
# Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

# The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2
# Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

# forward 5 adds 5 to your horizontal position, a total of 5.
# down 5 adds 5 to your depth, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13.
# up 3 decreases your depth by 3, resulting in a value of 2.
# down 8 adds 8 to your depth, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15.
# After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

# Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?



def find_position():
    """Find position of sub on Day 2 - part 1."""

    inputs = open_file()

    horizontal = 0
    depth = 0

    for item in inputs:
        if item[0] == "forward":
            horizontal += item[1]
        if item[0] == "backward":
            horizontal -= item[1]
        if item[0] == "up":
            depth -= item[1]
        if item[0] == "down":
            depth += item[1]

    return horizontal * depth

inputs2=[
    ('forward', 5),
    ('down', 5),
    ('forward', 8),
    ('up', 3),
    ('down', 8),
    ('forward', 2)
]

def find_position_pt2():
    """Find position of sub on Day 2 - part 2."""

    inputs = open_file()

    horizontal = 0
    depth = 0
    aim = 0

    inputs2=[
    ('forward', 5),
    ('down', 5),
    ('forward', 8),
    ('up', 3),
    ('down', 8),
    ('forward', 2)
]

    for item in inputs:
        print(f'item: {item}')
        if item[0] == "forward":
            horizontal += item[1]
            if aim > 0:
                add_depth = aim * item[1]
                depth += add_depth
        if item[0] == "backward":
            horizontal -= item[1]
        if item[0] == "up":
            aim -= item[1]
            # depth -= item[1]
        if item[0] == "down":
            aim += item[1]
            # depth += item[1]
        print(f'horizontal: {horizontal}')
        print(f'depth: {depth}')
        print(f'aim: {aim}')

    return horizontal * depth

print(find_position_pt2())