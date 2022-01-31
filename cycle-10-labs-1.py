# Author: ATN 1/31/22

def sums(n):
    # setting the starting values
    value = 0
    x = 0
    # adds each value to 1 plus itself
    while x < n:
        value += x + 1
        x += 1
    return value

print(sums(10))