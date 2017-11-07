import time
import math
from itertools import combinations, permutations
start = time.time()

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
       
p = permutations('012')

n = 8

a=[]
for i in range(3**n):
    a.append(str(baseN(i,3)).zfill(n))

b = set()
for i in p:
    s = ''.join(i)
    for j in a:
        for k in range(n-3+1):
            if s == j[k:k+3]:
                b.add(j)

print len(b)        
print(time.time() - start)        

