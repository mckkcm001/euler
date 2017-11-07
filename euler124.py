import time
import math
from operator import itemgetter

start = time.time()

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

rad=[]

n = 100000
for i in range(1,n+1):
    pfs = set(prime_factors(i))
    c = 1
    for j in pfs:
        c *= j
    rad.append([i,c])

sorted_rad = sorted(rad,key=itemgetter(1,0))
print sorted_rad[9999]
      
print time.time() - start        
