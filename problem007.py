import numpy as np
import math
import sys

def find_primes(n):
    primes = set(range(2,n+1))
    cur = 2
    while cur <= n/2:
        i = 2*cur/n
        sys.stdout.write("Progress: %3f\r" %i)
        poplist = set(range(cur*2, n+1, cur))
        primes = set([ p for p in primes if not p in poplist ])
        cur = min(p for p in primes if p > cur)

    print(f'percentage of primes: {len(primes)/n}')
    return primes
