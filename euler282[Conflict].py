import time
import math
from itertools import combinations
start = time.time()

a={}
a[(0,0)]=1

def acker(m,n):
    if m == 0:
        return n+1
    if n == 0:
        return acker(m-1,1)
    return acker(m-1,acker(m,n-1))

print acker(4,4)    
print(time.time() - start)        

