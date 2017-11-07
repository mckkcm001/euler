import time
start = time.time()
import math
from fractions import gcd
import itertools

def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1

    return amount
    
def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]
    
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

def product(list):
    p = 1
    for i in list:
        p *= i
    return p

def rad(n): 
    return product(set(prime_factors(n)))

r = {}
for n in range(1,120000):
    r[n]=rad(n)

#tot=[i for i in range(1,120000) if i-1 == phi(i)]
    
s = 0
n = 0
#p = rwh_primes1(int(math.sqrt(120000))+1)
for c in range(3,120000):
    for a in range(1,c/2+1):
        b = c - a
        if r[a]*r[b]*r[c] < c and gcd(a,c) == 1 and gcd(a,b) == 1 and gcd(b,c) == 1:  
            s += c
            n += 1
            #print n,a,b,c
            #print prime_factors(a)
            ##print prime_factors(b)
            #print prime_factors(c)
 
print n,s 
         
print time.time() - start

