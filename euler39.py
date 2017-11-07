from collections import Counter
import time
a = Counter()
p = {}
start = time.clock()
for i in range(1,998):
  for j in range(1,999-i):
    for k in range(int((i*i+j*j)**.5),1000-i-j):
      if i*i + j*j == k*k:
        p[(i,j,k)] = i + j + k

for v in p:
  a[p[v]] += 1

print(a.most_common(1))

print(time.clock() - start)
