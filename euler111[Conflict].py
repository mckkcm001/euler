import time

start = time.time()

import numpy
def primes(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]
 
a = primes(100000)   

M={}
N={}
S={}

for i in range(10):
    M[10,i]=0
    N[10,i]=0
    S[10,i]=0  
    for j in range(9,0,-1):
        for n in a:
            if str(n).count(str(i)) == j:
                M[10,i]=j
                N[10,i]+=1
                S[10,i]+=n
        if M[10,i] != 0:
            break
    print i,M[10,i],N[10,i],S[10,i]
        
print sum(S.values())
print time.time() - start        