import time
from itertools import permutations, combinations,product
start = time.clock()

def prime(n):
  if n%2 == 0: return False
  for i in range(3,int(n**.5)+1,2):
    if n%i == 0: return False
  return True

p=[]
for i in range(3,100001,2):
  if prime(i):
    p.append(i)

n=1000
p3=[]
for i1 in range(n):
  for i2 in range(i1+1,n+1):
    if prime(int(str(p[i1])+str(p[i2]))) and prime(int(str(p[i2])+str(p[i1]))):
        p3.append((p[i1],p[i2]))
p4=[]
for i in p3:
  for i3 in range(n):
    if p[i3] > i[0] and p[i3] > i[1]:
      if prime(int(str(p[i3])+str(i[0]))) and prime(int(str(i[0])+str(p[i3]))):
        if prime(int(str(p[i3])+str(i[1]))) and prime(int(str(i[1])+str(p[i3]))):
          p4.append((i[0],i[1],p[i3]))
          #print((i[0],i[1],p[i3]))

p5=[]
for i in p4:
  for i4 in range(n):
    if p[i4] > i[0] and p[i4] > i[1] and p[i4] > i[2]:
      if prime(int(str(p[i4])+str(i[0]))) and prime(int(str(i[0])+str(p[i4]))):
        if prime(int(str(p[i4])+str(i[1]))) and prime(int(str(i[1])+str(p[i4]))):
          if prime(int(str(p[i4])+str(i[2]))) and prime(int(str(i[2])+str(p[i4]))):
            p5.append((i[0],i[1],i[2],p[i4]))
            #print((i[0],i[1],i[2],p[i4]))

p6=[]
n=2000
for i in p5:
  for i5 in range(n):
    if p[i5] > i[0] and p[i5] > i[1] and p[i5] > i[2] and p[i5] > i[3]:
      if prime(int(str(p[i5])+str(i[0]))) and prime(int(str(i[0])+str(p[i5]))):
        if prime(int(str(p[i5])+str(i[1]))) and prime(int(str(i[1])+str(p[i5]))):
          if prime(int(str(p[i5])+str(i[2]))) and prime(int(str(i[2])+str(p[i5]))):
            if prime(int(str(p[i5])+str(i[3]))) and prime(int(str(i[3])+str(p[i5]))):
              p6.append((i[0],i[1],i[2],i[3],p[i5]))
              print((i[0],i[1],i[2],i[3],p[i5]))
print(p6)

print(time.clock() - start)
