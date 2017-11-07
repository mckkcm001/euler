import time
from itertools import permutations, combinations
start = time.clock()

t = 0
for i in range(1,10000):
  a = str(i)
  for j in range(100):
    p = int(a) + int(a[::-1])
    if j == 50:
      t += 1
      break
    if str(p) == str(p)[::-1]:
      break
    a = str(p)

print(t)
    
print(time.clock() - start)
