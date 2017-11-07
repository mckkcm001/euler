import math

n = [2]

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_circ(n):
    a = n
    for i in range(len(str(n))):
        a = 10**(len(str(a))-1)*(a%10)+ a//10
        if not is_prime(a):
            return False
    return True
        
    
for i in range(3,1000000,2):
    if i%10 == 0:
        continue
    if is_circ(i):
        n.append(i)
        
print(len(n))
