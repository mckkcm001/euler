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

s = [2]
for i in range(3,1000000):
  if is_prime(i):
    s.append(i)

n3 = 1
n1m = 0
n2m = 0
for i in range(len(s)-1):
  n1 = i
  m = s[i]
  n2 = n1
  for j in range(i+1,len(s)):
    m += s[j]
    if  m > 1000000:
      break
    else:
      if is_prime(m):
        n2 = j
  if n2 - n1 > n3:
    n3 = n2 - n1
    n2m = n2
    n1m = n1
      
a=0
for i in range(n1m,n2m+1):
  a += s[i]
  
print(n2m-n1m,a)

print(time.clock() - start)
