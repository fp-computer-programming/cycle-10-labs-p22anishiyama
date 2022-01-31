# Author: ATN 1/31/22

def divisibility(lst):
    values = []
    for x in lst:
        if(x > 500):
            break
        elif x % 5 == 0 and x <= 150:
            values.append(x)
    return values


print(divisibility([5, 10, 15, 17, 20, 160, 35, 501, 15]))