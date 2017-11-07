import time
import math

start = time.time()

def sumdig(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s

a = []
for i in range(1,100):
    for j in range(1,40):
        n = int(math.pow(i,j))
        if n > 9 and sumdig(n) == i:
            a.append(n)
a.sort()
for i in range(len(a)):
    print 1+i,a[i]

print time.time() - start        
