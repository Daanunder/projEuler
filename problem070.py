from primeClass import *
import itertools
from operator import itemgetter, attrgetter

## sort the first 10k numbers based on how few primefactors they have
## only check the first 1000
#def sort_and_sieve(numbers):
    #for n in numbers:

## check if the number has a permutation that is smaller than itself and how many
#def totient_potential_permutation_percentage(n):
    #perm = list(itertools.permutations(n))
    #denom =  
    #l = [int(''.join(x)) for x in perm if int(''.join(x)) < 58541]
## 


def find_minimum(primes=None):
    if not primes:
        primes = primeClass()
    step = 10000
    levels = 3
    for inc in range(1, levels):
        print(f"\n--------- STEP {step*inc} --------------")
        primes.find_primes(step*inc) 
        checklist = []
        for n in range((inc-1)*step, inc*step):
            l = get_permutations(n)
            if len(l) == 0:
                continue
            
            if n in primes.primes:
                checklist.append([n, 0, 0, l, None])
            else:
                # Get the primefactors of this number
                pf = primes.get_prime_factors(n)
                c = [n, len(l), len(pf), l, pf]
                checklist.append(c)

        checklist = sorted(checklist, key=itemgetter(1), reverse=True)
        checklist = sorted(checklist, key=itemgetter(2))
        for c in checklist:
            if not c[4]:
                phi = c[0] - 1
            else:
                phi = get_phi(c[0], c[4])
            r = c[0]/phi
            if phi in c[3]:
                print(r, c)

def get_phi(n, factors):
    non_rel_primes = set(factors)
    for f in factors:
        for i in range(2, round(n/f)):
            non_rel_primes.add(i*f)

    rel_primes = set(range(2,n)) - non_rel_primes
    rel_primes.add(1)
    phi = len(rel_primes)
    return phi

def get_permutations(n):
    perm = list(itertools.permutations(str(n)))
    l = set([ int(''.join(x)) for x in perm if (x[0] != '0' and int(''.join(x)) < n) ])
    return l


def search_minimum(increase=True):
    prime_c = primeClass()
    N = 10**6
    r = 2
    f = 3600
    found = False
    while not found:
        #primes = prime_c.find_primes(int(N**(1/r)+f))
        primes = prime_c.find_primes(int(f))
        if r > len(primes):
            print("FAILED")
            break

        combinations_of_primes = list(itertools.combinations_with_replacement(primes, r))
        comb_prods = [(x, np.prod(x), np.prod(x)*np.average(x)) for x in combinations_of_primes if np.prod(x) < N]
        comb_prods = sorted(comb_prods, key=itemgetter(2), reverse=True)
        print(r)
        for comb, prod, avg in comb_prods:
            perm = get_permutations(prod)
            if len(perm) == 0:
                continue
            
            substract = sum([int(prod/c) - 1 for c in comb])
            phi = prod - 1 - substract
            
            if phi in perm:
                print(f"SUCCES: {prod, phi, prod/phi}")
                #found = True
                #break

        r += 1
