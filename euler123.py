import time
import math

start = time.time()

import numpy
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]
        
def remainder(a,n):
    r1 = (n*(a-1)%(a*a))%(a*a)
    r2 = (n*(a+1)%(a*a))%(a*a) 
    return (r1+r2)%(a*a)

primes = primesfrom2to(100)
#print primes
#print len(primes)
c=0
for i in primes:
    c+=1
    #print c,  i, remainder(i,c)
    if remainder(i,c) > 9e8:
        print c,  i, remainder(i,c)
        if c> 7300:
            break

print time.time() - start        
