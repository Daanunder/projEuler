from problem003 import check_factors
import numpy as np

n_max = 500000

def search(n_min=100000, n_max=120000, max_res=0, target=1000):
    N = range(n_min, n_max)
    #factors = []
    for n in N:
        #f = len([ x for x in check_factors(n) if x < np.sqrt(n)])
        #factors.append(f)
        res = diophantines(n)
        l = len(res)
        if l > target:
            print("GOT IT:", n, l)
            return n, l
            #print("%08d" % n, "%03d" % len(res), "%020d" % int(bin(n)[2:]), sum(res)/len(res)/n)
        if l >= max_res:
            print("%08d" % n, "%03d" % len(res))
            max_res = l
    return 0, max_res

def diophantines(n):
    factors = [1,n]
    for i in range(2,n):
        if n**2 % i == 0:
            factors.append(i)
    return factors

def search2(n_min, n_max, flim, target=1000):
    search_list, factors = get_search_list(n_min, n_max, flim)
    lenghts = []
    max_res = 0 
    for i, n in enumerate(search_list):
        f = factors[i]
        res = diophantines(n)
        l = len(res)
        lenghts.append(l)
        print("%08d" % n, "%03d" % len(res), "%04d" % f)
        if l == target:
            print("GOT IT")
            #print("%08d" % n, "%03d" % len(res), "%020d" % int(bin(n)[2:]), sum(res)/len(res)/n)
        #if l >= max_res:
            #print("%08d" % n, "%03d" % l, f, l/f, factors)
            #max_res = l
    return search_list, lenghts

def get_search_list(n_min, n_max, flim):
    N = range(n_min, n_max)
    search_list = []
    factors = []
    for n in N:
        f = len(check_factors(n))
        if f > flim: 
            print("Found:", n, f)
            search_list.append(n)
            factors.append(f)
    return search_list, factors
