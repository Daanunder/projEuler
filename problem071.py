from primeClass import *

primes = primeClass()

def find_fraction():
    cur_max = 0
    f = 3/7
    for denom in range(2, 10**6):
        nom = int(f*denom)
        d = nom/denom
        if d > cur_max and d < f:
            cur_max = d
            solution = [nom, denom]

    print("Answer:", primes.reduce_fraction(solution[0], solution[1]))


