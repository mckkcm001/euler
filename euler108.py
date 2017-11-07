import time
from itertools import combinations
start = time.time()

s=0
for j in combinations([2,3,4,5,6,7,8,9,10,11,12,13],6):
    n = 1    
    for i in j:
        n *= i
    s = 0
    for i in range(1,n+1):
       if 1.*n*(n+i)/i == int(1.*n*(n+i)/i):
           s += 1
    if s > 1000 and s < 1020:
        print n, s    
print(time.time() - start)        

