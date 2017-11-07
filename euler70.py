import time
start = time.clock()

from fractions import gcd

def perm(a,b):
    a = list(str(a))
    b = list(str(b))
    a.sort()
    b.sort()
    if a == b:
        return True
    return False

def totient_sieve(n):
    ''' return list of totient(i) for i from 0 to n-1.
 
    >>> totient_sieve(12)
    [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10]
    '''
     
    tots = [x for x in range(n)]
    for i in range(2, n):
        if tots[i] == i:
            tots[i::i] = (x*(i-1)//i for x in tots[i::i])
    return tots

s = 10
phi = 1
tot = totient_sieve(10000001)
for i in range(2,len(tot)):
    t = tot[i]
    if perm(t,i):
        #print(i,t,i/t)
        if i/t < s:
            s = i/t
            phi = i

print(phi,s)

print(time.clock() - start)
