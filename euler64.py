import time
from fractions import Fraction
start = time.clock()

def cf(R):
  if (R**.5)==int(R**.5): return None
  a=[]
  n=[]
  d=[]
  c=0
  a.append(int(R**.5))
  n.append(int(R**.5))
  d.append(1)
  for i in range(a[0],0,-1):
    if ((i+n[c])*d[c])%(R-n[c]*n[c]) == 0:
      a.append((i+n[c])*d[c]//(R-n[c]*n[c]))
      n.append(i)
      d.append((R-n[c]*n[c])//d[c])
      c=1
      break
    
  while(True):
    for i in range(a[0],0,-1):
      if ((i+n[c])*d[c])%(R-n[c]*n[c]) == 0:
        a.append((i+n[c])*d[c]//(R-n[c]*n[c]))
        n.append(i)
        d.append((R-n[c]*n[c])//d[c])
        c+=1
        break
      
    if a[c] == a[1] and n[c] == n[1] and d[c] == d[1]:
      #print(R,R**.5,a,n,d)
      return c%2 == 0
       
s = 0
for i in range(2,10001):
  if cf(i):
    s += 1
    
print(s)

print(time.clock() - start)
