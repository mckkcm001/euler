import time
from itertools import permutations, combinations
start = time.clock()

def is_prime(n):
  if n%2 == 0:
    return False
  for i in range(3,int(n**.5)+1,2):
    if n%i == 0:
      return False
  return True

for i in range(100001,990000,2):
  if is_prime(i):
    i1 = [int(k) for k in str(i)]
    for j in range(2,64,2):
      j1 = [0,0,0,0,0,0]
      j1[0] = j//32
      j1[1] = (j%32)//16
      j1[2] = (j%16)//8
      j1[3] = (j%8)//4
      j1[4] = (j%4)//2
      n=0
      a=[]     
      for r1 in range(10):
        p=0
        for d in range(6):
          if j1[d] == 0: p+= i1[d]*10**(5-d)
          else: p+= r1*10**(5-d)
        
        if is_prime(p):
          n+=1
          a.append(p)
      if n == 8:
         print(a)

print(time.clock() - start)
