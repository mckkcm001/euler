import time
from itertools import permutations
start = time.time()

n = 9

tot = 1 # no red pieces

# 1 red piece length 3 to n
# (n-2)(n-1)/2 combos
tot = tot + (n-2)*(n-1)/2

# 2 red pieces length 3 to n-4
red=[]
rmin=3
rmax = n-4
for d1 in range(rmin,rmax+1):
    for d2 in range(rmin,rmax+1+rmin-d1):
        red.append([d1,d2])
print red
for i in red:
    b = n-i[0]-i[1]
    print i,b
    tot = tot + (b)*(b+1)/2
    
print n,tot

print time.time() - start