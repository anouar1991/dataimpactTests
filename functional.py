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


def sum_consecutives(lst):
    sum_list = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            sum_list[len(sum_list)-1] = sum_list[len(sum_list)-1] + lst[i]
        else:
            sum_list.append(lst[i])
    return sum_list


if __name__ == "__main__":
    print("Testing Function sum_int(['1','2','n']:")
    print(sum_int(['1', '2', 'n']))
    print("Testing Function persistence(5):")
    print(persistence(5))
    print("Testing Function sum_consecutives([-5, -5, 7, 7, 12, 0]):")
    print(sum_consecutives([-5, -5, 7, 7, 12, 0]))
