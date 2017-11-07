import time
from itertools import permutations
start = time.clock()
a = [1,2,3,4,5,6,7]

def is_prime(n):
  if n%2 == 0:
    return False
  for i in range(3,int(n**.5)+1):
    if n%i == 0:
      return False
  return True

max = 0
for i in permutations(a):
  n = ''
  for j in i:
    n += str(j)
  n = int(n)
  if is_prime(n):
    if n > max:
      max = n
print(max)

print(time.clock() - start)
