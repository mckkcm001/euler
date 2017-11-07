import time
from itertools import permutations, combinations
start = time.clock()

def fact(n):
  if n == 1 or n == 0: return 1
  return n*fact(n-1)

m=0
for n in range(1,101):
  for r in range(1,n+1):
    if fact(n)/fact(r)/fact(n-r) > 1000000:
      m += 1
print(m)
    
print(time.clock() - start)
