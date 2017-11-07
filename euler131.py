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

primes = primesfrom2to(1000000)
#print primes
#print len(primes)
c=0
for p in primes:
    for b in range(1,int(4*p/3)+1):
        disc=b*math.sqrt(b*(4*p-3*b))
        if disc == math.floor(disc):
           
            #n = (-3*b*b + disc)/2/(3*b-p)
            #if n == math.floor(n) and  n >= 1:
                #print p,n,n+b
                #c+=1

            n = (-3*b*b - disc)/2/(3*b-p)
            if n == math.floor(n) and  n >= 1:
                #print p,n,n+b
                c+=1

print c

print time.time() - start        
