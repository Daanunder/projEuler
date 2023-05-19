import numpy as np
import math
import sys
from collections import OrderedDict


class primeClass:
    def __init__(self):
        self.cur_max = 2
        self.primes = OrderedDict()
        self.primes[2] = 0
    
    def find_primes(self, n):
        if self.cur_max >= n:
            p = OrderedDict()
            for k in self.primes:
                if k > n:
                    break
                else:
                    p[k]=0
            return p

        else:
            primes = self.primes
            for k in range(self.cur_max+1, n+1):
                self.primes[k] = 0
            
            index = 0
            it_list = self.primes.copy()
            for cur in it_list:
                start = max(cur*int(self.cur_max/cur), cur*2)
                poplist = range(start, n+1, cur)
                for i in poplist:
                    self.primes.pop(i, None)

            self.cur_max = n
            return self.primes

    def get_prime_factors(self, n):
        primes = self.find_primes(int(n/2))
        primefactors = dict()
        for p in primes:
            i = n
            while i > 1:
                q = i / p
                if q % 1 == 0:
                    i = q
                    if primefactors.get(p):
                        primefactors[p] += 1
                    else:
                        primefactors[p] = 1
                else:
                    i = 1
        return primefactors

    def get_factors(self, n):
        primes = self.find_primes(int(n/2+1))
        factors = set()
        if self.is_prime(n):
            return factors
        else:
            done = False
            power = 0
            checklist = [n]
            while not done:
                new_checklist = []
                for n in checklist:
                    for p in primes:
                        d = n/p
                        if d % 1 == 0:
                            new_checklist.append(int(d))
                            factors.add(int(d))
                            factors.add(int(p))
                if new_checklist:
                    checklist = new_checklist
                else:
                    done = True
            return factors


    def get_totient(self, n):
        # find non_rel_primes of n
        factors = self.get_factors()
        non_rel_primes = set(factors)
        for f in factors:
            for i in range(2, round(n/f)):
                non_rel_primes.add(i*f)
        
        # get relative primes and phi(n)
        rel_primes = set(range(2,n)) - non_rel_primes
        rel_primes.add(1)
        phi = len(rel_primes)
        return n/phi

    def is_prime(self, n):
        for i in reversed(range(2, int(n/2)+1)):
            if n % i == 0:
                return False
        return True

    def reduce_fraction(self, nom, denom):
        nom_f = self.get_prime_factors(nom)
        denom_f = self.get_prime_factors(denom)
        isect = set(nom_f).intersection(set(denom_f))
        if isect:
            done = False
            new = True
            while not done:
                if new:
                    try:
                        f = isect.pop()
                        new = False
                    except KeyError:
                        done = True
                if nom/f % 1 == 0 and denom/f % 1 == 0:
                    nom = int(nom/f)
                    denom = int(denom/f)
                else:
                    new = True
        return nom, denom
