import time
start = time.time()
from fractions import gcd, Fraction


def totient1(n):
    unique = []
    totient = 1
    for p in prime_factors(n):
        if p not in unique:
            unique.append(p)
            totient *= p-1
        else:
            totient *= p
    return totient
    
    
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

for n in range(10,100):      
    a = Fraction(totient1(n),n-1)
    print float(a)
    if a < Fraction(15499,94744):
        print n-1
        break
    
         
print time.time() - start

