import numpy as np
import math

def palindrom_check(n):
    for i in reversed(range(n)):
        if list(str(i)) == list(reversed(str(i))):
            f = check_factors_edit(i)

            if any(all(len(list(str(x))) < 4 for x in y) for y in f):
                print(f[0])
                break
                #print(z if all(len(list(str(w))) < 3 for w in z) for z in f)


def check_factors_edit(n):
    factors = []
    # Finding factors of a number
    for i in reversed(range(1,math.ceil(np.sqrt(n)))):
        if n % i == 0:
            factors.append([i, int(n/i)])

    return factors
            
