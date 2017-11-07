import time
from itertools import permutations
start = time.clock()

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

for i in range(100000,300000):
  if len(set(prime_factors(i))) >= 4 and \
     len(set(prime_factors(i+1))) >= 4 and \
     len(set(prime_factors(i+2))) >= 4 and \
     len(set(prime_factors(i+3))) >= 4:
    print(i,i+1,i+2,i+3)
    break

print(time.clock() - start)
