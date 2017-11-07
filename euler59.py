import time
start = time.clock()

with open('cipher1.txt') as f:
  a = f.read().splitlines()
a = a[0].split(',')

for k1 in range(103,104):
  for k2 in range(111,112):
    for k3 in range(100,101):
      s = ''
      for i in range(0,len(a),3):
        s += chr(int(a[i])^k1)
        if i+1 < len(a): s += chr(int(a[i+1])^k2)
        if i+1 < len(a): s += chr(int(a[i+2])^k3)
      if 'the' in s and 'and' in s: print(k1,k2,k3,s)

t = 0
for i in s:
  t += ord(i)

print(t)

print(time.clock() - start)
