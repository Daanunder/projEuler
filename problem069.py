from problem003 import *
import numpy as np

def get_totient(n):
    # find non_rel_primes of n
    factors = check_factors(n)
    non_rel_primes = set(factors)
    for f in factors:
        for i in range(2, round(n/f)):
            non_rel_primes.add(i*f)
    
    # get relative primes and phi(n)
    rel_primes = set(range(2,n)) - non_rel_primes
    rel_primes.add(1)
    phi = len(rel_primes)
    return n/phi

def max_totient(stop, start=2):
    T = []
    M = []
    max_tot = 0
    for n in range(start, stop):
        tot = get_totient(n)
        if tot > max_tot:
            max_tot = tot
            print(n, max_tot)
    return max_tot

## Just multiply all primes starting below a limit, given this product is smaller than 1.000.000. This gives np.prod(find_primes(17)) = 510510.
