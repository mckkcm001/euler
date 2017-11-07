import time
from itertools import permutations
start = time.clock()
p = []

for i in range(1,10000):
    p.append(i*(3*i-1)/2)

d = 100000
for i in range(len(p)-1):
  for j in range(i+1,len(p)):
    if (p[j]+p[i] in p) and (p[j] - p[i] in p):
      print(p[j],p[i],p[j]+p[i],p[j] - p[i])
      if d > p[j] - p[i]:
        d = p[j] - p[i]

print(d)

print(time.clock() - start)
