from itertools import combinations, permutations
from fractions import Fraction
import time

start = time.time()

def get_max(r):
    for i,j in enumerate(r):
        if i+1 != j:
            return i
    return len(r)

m1 = 0
for k in combinations('0123456789',4):
    r = set()
    m = 0
    for i in permutations(k,4):
        for j in permutations('***///+++---',3):
            s = i[0]+j[0]+i[1]
            try:
                #print s
                a = eval(s)
                #print a
            except:
                continue               
            s = str(a)+j[1]+i[2]
            try:
                #print s
                a = eval(s)
                #print a
            except:
                continue
            s = str(a) +j[2]+i[3]
            try:
                #print s
                a = eval(s)
                #print a
            except:
                continue
            if a == int(a) and a > 0:
                r.add(a)
    r = sorted(list(r))
    for i,j in enumerate(r):
        if i + 1 == j:
            m += 1
        else:
            break
    if m > m1:
        print k, m, r[:m]
        m1 = m
            
print(time.time() - start)        
