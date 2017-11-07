import copy
import time

t1 = time.time()

with open('triangle.txt') as tri:
  b = tri.readlines()

for i in range(0,len(b)):
  b[i] = b[i].split()

for i in range(0,len(b)):
  for j in range(0,len(b[i])):
    b[i][j] = int(b[i][j])

c = copy.deepcopy(b)
t2 = time.time()

for i in range(1,len(b)):
  for j in range(0,len(b[i])):
    if j == 0: 
      c[i][j] = b[i][j]+c[i-1][j]
    if j == len(b[i])-1: 
      c[i][j] = b[i][j]+c[i-1][j-1]
    else: 
      if c[i-1][j] > c[i-1][j-1]:
        c[i][j] = b[i][j]+c[i-1][j]
      else:
        c[i][j] = b[i][j]+c[i-1][j-1]

t3 = time.time()
print("%3.2f ms" % ((t2 - t1) * 1000))
print("%3.2f ms" % ((t3 - t2) * 1000))
print(max(c[len(b)-1]))
