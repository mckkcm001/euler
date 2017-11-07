import math

max = 1
for i in range(12,1000000):
  n = i
  chain = 1
  while n != 1:
    if n % 2 == 0:
      n = n/2
    else:
      n = 3*n + 1
    chain+=1
  if chain > max:
    max = chain
    maxn = i
print(maxn)
