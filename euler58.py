import time
start = time.clock()

def prime(n):
  if n%2 == 0: return False
  for i in range(3,int(n**.5)+1,2):
    if n%i == 0: return False
  return True

s = 0
for i in range(2,30000,2):
  if prime(i*i+1):
    s += 1
  if prime(i*i+1-i):
    s += 1
  if prime(i*i+1+i):
    s += 1
  if (2*i+1)/s > 10:
    print(i)
    break

print(time.clock() - start)
