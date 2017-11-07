import time
import math

start = time.time()

def remainder(a,n):
    r1 = (n*(a-1)%(a*a))%(a*a)
    r2 = (n*(a+1)%(a*a))%(a*a) 
    return (r1+r2)%(a*a)

sum = 0
for i in range(3,1001):
    rmax = 0
    for j in range(1,i):
        if remainder(i,j) > rmax:
            rmax = remainder(i,j)
    sum += rmax
    
print sum

print time.time() - start        
