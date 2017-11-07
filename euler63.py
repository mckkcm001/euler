import time
from itertools import permutations, combinations,product
start = time.clock()

t=0
for i in range(1,100):
  for n in range(1,100):
    if len(str(i**n)) == n:
      t += 1
      print(t,i,n,i**n)

print(time.clock() - start)
