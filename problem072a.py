from primeClass import *
import itertools
primes = primeClass()

#### 
## for all d
    ## get prime_factors
## for all prime_factors
    ## q = r(d/f) 
    ## substract q - 1
    ## add count other factors that are lower than q but higher than f
    ## 

#### 

#### 
## starting from low to high
## check if it is a prime
    ## add p: p - 1 to dict
## else  
    ## divide by prime
    ## check if the result is in dict
        ## add val of result to current
    ## else
        ## A
####


####
## for n in range(1, 10**7)
    ## find primefactors for n:
        ## substract = SUM( ((10**7 - n) / pf) - 1 ) for pf in primefactors
        ## get product of all combinations, selecting s [2 - all]
        ## compensate = SUM( (((10**7 - n) / cb) - 1)*(s-1) for db in combinations
    ## 10**7 - n - substract + compensate
####



def calc_rpfs(N):
    total_rpf = 0
    for n in range(1, N):
        rpf_n = N - n - 1
        primefactors = primes.get_prime_factors(n)
        substract = sum([int((N - n) / pf) - 1 for pf in primefactors])
        rpf_n -= substract
        usable_factors = primefactors.keys()
        compensate = 0
        overcompensated = 0
        s_max = len(usable_factors)
        for s in reversed(range(2, s_max+1)):
            combinations = list(itertools.combinations(usable_factors, s))
            compensate += sum((int((N - n) / np.prod(cb)) - 1)*(s-1) for cb in combinations)
            if s > 2:
                overcompensated = int(sum([n/np.prod(cb) * s for cb in combinations]))

            ## TODO: Check wich cb's generate overlapping compensation
            ## N/cb
            
        rpf_n += compensate - overcompensated
        total_rpf += rpf_n
    return total_rpf

####
## first add all primes (d - 1)
## then do n=1:
## add all d that are not prime
## then do n=2, same as above but then for numbers up to N/2
## add all d below N/2 that are not prime
## Do it for all numbers
## n = 6, d up to N/
####


def ncr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def check_rpf(N):
    res = 0
    for i in range(2,N+1):
        res += single_rpf(i)
    return res

def single_rpf(n):
    pf_n = primes.get_prime_factors(n)
    substract = 0
    for i in range(2, n):
        if any(p in primes.get_prime_factors(i).keys() for p in pf_n):
            substract += 1
    return n - 1 - substract - len(pf_n)

