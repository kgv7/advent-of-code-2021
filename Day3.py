# Day 3

# You need to use the binary numbers in the diagnostic report to 
# generate two new binary numbers (called the gamma rate and the 
# epsilon rate). The power consumption can then be found by multiplying 
# the gamma rate by the epsilon rate.

def open_file():
    """Create list of inputs for Day 2 Advent of Code."""

    file = open("inputs-day3.csv")

    inputs = []

    for line in file:
        line = list(line.rstrip())
        inputs.append(line)

    return inputs

# print(open_file())


# gamma rate takes most common bit from each binary num, put together, then convert to decimal

def get_gamma():
    """Find gamma rate of submarine - Day 3 part 1."""

    inputs = open_file()
    gamma = []
    print(inputs)
    i = 0

    # while i < len(inputs):

    for item in inputs:
        one = 0
        zero = 0
        
        for char in item:
            if char == "1":
                one += 1
            if char == "0":
                zero += 1

        if one > zero:
            gamma.append("1")
        else:
            gamma.append("0")
        
        # i+=1
    
    gamma = "".join(gamma)
    return gamma

print(get_gamma())


# The epsilon rate is calculated in a similar way; rather than use the 
# most common bit, the least common bit from each position is used. So, 
# the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate 
# (22) by the epsilon rate (9) produces the power consumption, 198.

def get_epsilon():
    """Find epsilon rate of submarine - Day 3 part 1."""

    inputs = open_file()
    epsilon = []

    for line in inputs:
        one = 0
        zero = 0
        # print(f"line: {line}")
        for char in line:
            # print(f"char: {char}")
            if char == "1":
                one += 1
            if char == "0":
                zero += 1
        # print(f'one: {one}')
        # print(f"zero: {zero}")
        if one > zero:
            epsilon.append("0")
        else:
            epsilon.append("1")
    
    epsilon = "".join(epsilon)
    return epsilon

# print(get_epsilon())

