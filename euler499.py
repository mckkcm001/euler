from fractions import Fraction
import random
import time
import itertools
start = time.time()

L2={1:1}  

for level in range(20):
    for x in range(2,10000):    
        s = 0
        for n in range(level+1):       
            if x-2+2**n in L2:
                #print level,x,n, L2
                s += L2[x-2+2**n]/2.0**(n+1)
            L2[x] = s

print 1-L2[2]
print time.time() - start