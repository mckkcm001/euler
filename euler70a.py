import time
start = time.clock()

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

print(len(totient_sieve(1000000)))

def gen_primes():
  D = {}
  q = 2  # first integer to test for primality.

  while True:
    if q not in D:
      # not marked composite, must be prime  
      yield q 

      #first multiple of q not already marked
      D[q * q] = [q] 
    else:
      for p in D[q]:
        D.setdefault(p + q, []).append(p)
      # no longer need D[q], free memory
      del D[q]

    q += 1

a=[]    
primes = gen_primes()
for p in primes:
  a.append(p)
  if p > 1000000: break

index = 0  
def primesbelow(n):
    while a[index] < n:
        index += 1
    return a[0:index]

s = 10
phi = 10
t = totientsbelow(100)
for i in t:
    print(i)
    
print(time.clock() - start)
