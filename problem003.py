import numpy as np
import math
import sys


def find_primes(n):
    primes = range(2,n+1)
    index = 0
    cur = primes[index]
    while cur <= n/2:
        poplist = range(cur*2, n+1, cur)
        primes = [ p for p in primes if not p in poplist ]
        index += 1
        cur = primes[index]
    return primes


def get_prime_factors(n):
    primes = find_primes(n)
    primefactors = []
    for p in primes:
        if p > np.sqrt(n):
            break
        if n % p == 0:
            primefactors.append(p)
    return primefactors


def get_factors(n):
    primefactors = get_prime_factors(n)
    factors = []
    for p in primefactors:
        factors.append(p)
    return factors
