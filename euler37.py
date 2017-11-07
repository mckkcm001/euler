import math

n = []

def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_trunc(n):
    a = n
    for i in range(len(str(a))):
        if not is_prime(a):
            return False
        a = a//10
    a = n
    for i in range(len(str(a))):
        if not is_prime(a):
            return False
        a = a%(10**(len(str(a))-1))    
    return True
        
for i in range(11,1000000,2):
    if is_trunc(i):
        n.append(i)
        
print(sum(n))
