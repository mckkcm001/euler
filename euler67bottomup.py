import copy
import time

t1 = time.time()

with open('triangle.txt','r') as f:
    b = [[int(i) for i in r.split()] for r in f.readlines()]

t2 = time.time()

for i in range(len(b)-1,0,-1):
    for j in range(0,len(b[i])-1):
      b[i-1][j] += max(b[i][j],b[i][j+1])
      
t3 = time.time()
print("%3.2f ms" % ((t2 - t1) * 1000))
print("%3.2f ms" % ((t3 - t2) * 1000))
print(b[0][0])
