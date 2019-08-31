import numpy as np


def sum_int(lst):
    return sum([int(n) for n in lst if n.isdigit()])


def rec_per(n, t):
    str_n = str(n)
    if len(str_n) == 1:
        return t
    mult = np.prod([int(n) for n in str_n])
    return rec_per(mult, t+1)


def persistence(n):
    return rec_per(n, 0)
