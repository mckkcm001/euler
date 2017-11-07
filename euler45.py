import time
from itertools import permutations
start = time.clock()
t = set()
p = set()
h = set()

for i in range(1,100000):
    t.add(int(i*(i+1)/2))
for i in range(1,100000):
    p.add(int(i*(3*i-1)/2))
for i in range(1,100000):
    h.add(i*(2*i-1))

print(t.intersection(p.intersection(h)))

print(time.clock() - start)
