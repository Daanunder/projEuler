import numpy as np
import math

def get_sum_square_diff(n):
    l = np.array([np.arange(1,n+1)])
    a = np.dot(l.T, l)
    print(a.sum() - a.diagonal().sum())
