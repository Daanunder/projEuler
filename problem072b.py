from primeClass import *
import math

## trivial solutions
# s = 100
# n = d - 1     => gives s-1 rpf's
# n = 1         => gives s-1 rpf's

## primes
# np = number of primes < s
#               => gives np * (s-1) rpf's 

## relative primes
# for t in s
# nrp = number of relatively prime < t
#               => gives nrp 


primes = primeClass()
#primes.find_primes(10**5)


def get_rel_primes(n, hard=False):
    p = primes.find_primes(n)
    f = primes.get_prime_factors(n).keys()
    pl = primes.find_primes(max(f))
    rp = set(p) - set(f)
    rpl = set(pl) - set(f)
    if not hard:
        rp.update(get_rp_multiples(list(rpl), n, list(rp)))
        rp.update(get_rp_complements(rp, n))
    else:
        rp.update(get_rp_multiples(list(rp), n, list(rp)))
        rp.update(get_rp_complements(rp, n))
    return rp

def get_rp_multiples(l, n, p):
    multiples = [] 
    for b in l:
        pop_list = p
        while pop_list:
            m = b
            r = pop_list.pop(0)
            while m < n:
                multiples.append(m)
                m = m * r
    return set(multiples)

def get_rp_complements(l, n):
    complements = []
    for c in l:
        complements.append(n-c)
    return complements
