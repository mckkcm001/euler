import time
import itertools
import math

start = time.time()

n = 12
a=[]
s = range(1,n+1)
for m in range(2,n/2+1):
    for i in itertools.combinations(s,m):
        c = list(i)
        b = [j for j in s if j not in i]
        #print c,b
        d = itertools.combinations(b,m)
        #print d
        for x in d:
            e = list(x)
            gt = False
            lt = False
            for t in range(0,m):
                if e[t] > c[t]:
                    gt = True
            for t in range(0,m):
                if e[t] < c[t]:
                    lt = True        
            if lt and gt:        
                a.append([c,e])

print len(a)/2



 

print(time.time() - start)        

