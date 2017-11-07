import time
from itertools import permutations, combinations
start = time.clock()



for x in range(100,1000000):
  if sorted(list(str(2*x))) == sorted(list(str(3*x))) == sorted(list(str(4*x))) == sorted(list(str(5*x))) == sorted(list(str(6*x))):
    print(x)
    break

print(time.clock() - start)
