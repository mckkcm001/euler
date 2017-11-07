import math
from itertools import combinations
print e
def f(n,k):
    return pow(e,1.*k/n)-1

n = 200
a = [(i,f(n,i)) for i in range(1,int(n*math.log(pi+1)))]    
s = 5
gm = 0
for i in combinations(a,4):
    tot = 0
    g = 0
    for j in i:    
        tot += j[1]
        g += j[0]*j[0]
    if abs(pi - tot) < s:
        s = abs(pi - tot)
        gm = g
print gm