import math

def isprime(n):
  for i in range(2,1 + int(math.pow(n,.5))):
    if n % i == 0:
      return False
  return True
  
a = 0

for b in range(2,2000000):
    if isprime(b):
      a+=b

print(a)

        
      
