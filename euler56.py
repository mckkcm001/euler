import time
from itertools import permutations, combinations
start = time.clock()

m = 0
for a in range(1,100):
  for b in range(1,100):
    n = a**b
    t = 0
    for i in str(n):
      t += int(i)
    if t > m:
      m = t

print(m)
    
print(time.clock() - start)
