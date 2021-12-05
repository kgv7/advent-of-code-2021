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
        line = line.rstrip()
        inputs.append(line)

    return inputs

print(open_file())