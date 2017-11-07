import time
import math

start = time.time()

def factors(n):    
  return set(reduce(list.__add__, 
    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def sigma2(n):
  return sum([i*i for i in factors(n)]) 

def is_square(n):
    b = math.sqrt(sigma2(n))
    return math.floor(b)==b
    
s=0
for i in range(1,64000000):
    if is_square(i):
        s+=1
        
print s                

print time.time() - start        
