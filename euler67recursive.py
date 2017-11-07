import time

t1 = time.time()

with open('triangle.txt','r') as f:
    b = [[int(i) for i in r.split()] for r in f.readlines()]

t2 = time.time()

def euler67(a):
  if len(a) == 1:
    print b[0][0]
  else:
    row1 = b[len(a)-1]
    row2 = b[len(a)-2]
    for i in range(0,len(row2)):
      row2[i] += max(row1[i],row1[i+1])
    return euler67(row2)

euler67(b[len(b)-1])

t3 = time.time()

print("%3.2f ms" % ((t2 - t1) * 1000))
print("%3.2f ms" % ((t3 - t2) * 1000))
