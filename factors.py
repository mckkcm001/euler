from itertools import combinations
from operator import mul
from copy import copy

def factors(n):   
    a = set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    a = sorted(list(a))
    a.pop()
    a.pop(0)
    b = []
    for i in range(len(a)//2):
        b.append([a[i],a[-1-i]])
    if len(a)%2 != 0 and len(a) != 0:
        b.append([a[len(a)//2],a[len(a)//2]]) 
    return b
    
def first_factor(n):
    p = first_prime(n)
    return [p,n//p]

def first_prime(n):
    d = 2
    while True:
        if n % d == 0:
            return d
        d = d + 1
        
def factorize(n):
    a = factors(n)
    for i in a:
        if first_prime(i[-1]) != i[-1]:
            for j in factors(i[-1]):
                a.append(list(i[0:-1])+j)
    g = set()    
    for i in a:
        g.add(tuple(sorted(i)))
    
    return g

d = {}
for n in range(4,25000):
    f = factorize(n)
    for i in f:
        c = sum(i)
        if c <= n:
            index = len(i) + n - c
            if index not in d: 
                d[index] = n
                    
s = set()
for i in range(2,12001):
    if i in d:        
        s.add(d[i])
    else:
        print i

print sum(list(s))
