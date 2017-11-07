import time
import math

start = time.time()

def increasing(a):
    n = str(a)
    for i in range(len(n)-1):
        if n[i:i+1] > n[i+1:i+2]:
            return False
    return True

def decreasing(a):
    n = str(a)
    for i in range(len(n)-1):
        if n[i:i+1] < n[i+1:i+2]:
            return False
    return True

c1 = 0
c2 = 1
while (1.0*c1/c2 < 0.99):
    c2 += 1
    if increasing(c2) or decreasing(c2):
        pass
    else:
        c1 += 1

print c1,c2, 1.0*c1/c2

print time.time() - start        
