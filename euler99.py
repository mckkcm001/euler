import time
import math
start = time.clock()

with open('base_exp.txt') as tri:
  b = [line.rstrip().split(',') for line in tri]

m = 0
n = 0
for i,j in enumerate(b):
    print i,j
    man = int(j[0])
    exp = int(j[1])
    a = exp*math.log(man)
    if a > m:
        n = i
        m = a
print n
print(time.clock() - start)
