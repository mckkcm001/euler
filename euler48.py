import time
from itertools import permutations
start = time.clock()

s = 0
for i in range(1,1001):
  s += i**i

print (str(s)[-10:])

print(time.clock() - start)
