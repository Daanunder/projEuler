import numpy as np
import math 


def recursive_fibo(start, MAX, n, fibo_list):
    if start < MAX:
        n += 1
        fibo_list.append(start)
        start = fibo_list[-1] + fibo_list[-2]
        recursive_fibo(start, MAX, n, fibo_list)
        return fibo_list
    else:
        print(fibo_list)
        return fibo_list

def get_sum(MAX):
    final_list = recursive_fibo(1, MAX, 0, [1])
    rest = len(final_list) % 3
    if rest != 0:
        zeros = [0]*(3-rest)
        final_list.extend(zeros)
    l = np.reshape(final_list, (-1, 3))
    total = l.sum(axis=0)
    return total, l



