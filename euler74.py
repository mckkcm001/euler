import time
from collections import Counter
start = time.clock()

from numpy import matrix,array

def PrimPythTrips(max=None):
  '''generate all primative triples such that 
  the sum is less than or equal to max'''
  u=matrix( [[1,2,2], [-2,-1,-2], [2,2,3]] )
  a=matrix( [[1,2,2], [2,1,2], [2,2,3]] )
  d=matrix( [[-1,-2,-2], [2,1,2], [2,2,3]] )
  m=[ array([3,4,5]) ]
  while m:
    for i in m:
      yield i
    g=( (i*j).getA1() for i in m for j in (u,a,d) )
    m=[ i for i in g if max is None or sum(i)<=max ]

def AllPythTrips(max):
  '''generate all triples such that 
  the sum is less than or equal to max'''
  for i in PrimPythTrips(max):
    ret=i[:]
    while sum(ret)<=max:
      yield ret
      ret=ret+i

max = 1500000
t={}
for i in AllPythTrips(max):
  t[tuple(i)]=sum(i)

s=0
c=Counter(t.values())

for i in c:
  if c[i] == 1:
    s+=1
print(s)
print(time.clock() - start)
