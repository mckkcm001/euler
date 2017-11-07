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

for i in range(1000,10000):
  #print(i)
  if is_prime(i):
    a=[]
    for j in permutations(str(i)):
      #print(int(j[0])*1000+int(j[1])*100+int(j[2])*10+int(j[3]))
      if is_prime(int(j[0])*1000+int(j[1])*100+int(j[2])*10+int(j[3])):
        a.append(int(j[0])*1000+int(j[1])*100+int(j[2])*10+int(j[3]))
    a.sort()
    #print(a)
    
    if len(a) > 2:
      for j in range(len(a)-2):
        for k in range(j+1,len(a)-1):
          for m in range(k+1,len(a)):
            if a[m] - a[k] != 0 and a[m] - a[k] == a[k] - a[j] :
              print(a[j],a[k],a[m])


print(time.clock() - start)
