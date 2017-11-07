import time
from itertools import permutations
start = time.clock()

def is_prime(n):
  for i in range(3,int(n**.5)+1,2):
    if n%i == 0:
      return False
  return True

for i in range(5001,50000,2):
  if is_prime(i):
    #print(str(i) + ' is prime')
    continue
  gold = False
  for j in range(1,int(i**.5)+1):
    #print(str(i) + ' is composite minus ' + str(2*j*j) + ' = ' + str(i-2*j*j))
    if i - 2 < 2*j*j:
      break
    if is_prime(i - 2*j*j):
      gold = True
  if not gold:
    print(i)
    break

print(time.clock() - start)
