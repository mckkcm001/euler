import time
import math

start = time.time()

def ispalindrome(n):
    return str(n) == str(n)[::-1]
        
pal=[]
squares = []
n = 10010
for i in range(2,n):
    for j in range(1,n-i+1):
        sq = 0
        for k in range(j,j+i):
            sq += k*k
        if sq > 1e8:
            break
        if ispalindrome(sq):
            pal.append(sq)
            squares.append(range(j,j+i))

print pal 
print squares         
    
sumsq = long(0)
for i in pal:
   sumsq += i
print sumsq
print time.time() - start        
