from math import inf


def divide(num1, num2):
    if num2 != 0:
        res = num1 / num2
    else:
        return inf
    return res
