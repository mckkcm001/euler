import time
from fractions import Fraction
import random
start = time.time()

a='ROYGBIVROYGBIVROYGBIVROYGBIVROYGBIVROYGBIVROYGBIVROYGBIVROYGBIVROYGBIV'
a='ROYROY'
b=list(a)
m=0
t=0
for i in range(1000000):
    random.shuffle(b)
    c=''.join(b[0:3])
    s=0
    for i in 'ROY':
        if i in c:
            s+=1
    t+=1
    m+=s
    
print float(1.0*m/t)

print time.time() - start