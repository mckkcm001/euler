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
      return a

def normal_fraction(continued_fraction):
    n = Fraction(0)
    for d in continued_fraction[:0:-1]:
      n = 1 / (d + n)
    return continued_fraction[0] + n
        
s = 0
for i in range(61,62):
  if cf(i) == None: continue
  a = cf(i)
  a.pop(len(a)-1)
  if len(a)%2 != 0:
    a.pop(len(a)-1)
  print(a)
  print(normal_fraction(a))
    
print(s)

print(time.clock() - start)
