import time
from operator import itemgetter
start = time.time()

def factors(n):    
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

'''
find factors
find partition of factors (sage)
which partitions are  products 
which partition is minimal size
add to dictionary of number and partition size 
increase number and repeat
'''

def part(coins):
    final = [[0]*(len(coins))]
    final[0][0] = coins[-1]
    coins = coins[0:-1]
    
    for coin in reversed(coins):
        i = 0
        while i < len(final):
            combo = final[i]
    
            if combo[0] >= coin:
    
                newcombo = combo[:]
                newcombo[0] -= coin
    
                newcombo[coins.index(coin)+1] += 1
    
                final.append(newcombo)
    
            i += 1
    yield [i[1:] for i in final if i[0] == 0]
    
t = {}
for n in range(4,1000):
    facts = sorted(list(factors(n)))
    parts = part(facts)
    a = []
    for i in parts:
        s = 0
        p = 1
        for j,k in enumerate(i):
            if facts[j]*k != 0:
                s += facts[j]*k
                p *= facts[j]**k
        if s == p:
            a.append([sum(i),s])
    print n,a
    if a != []:
        for i in a:
            try:
                if t[i[0]] > i[1]:
                    t[i[0]] = i[1]
            except:
                t[i[0]] = i[1]
                          
print sum(list((set(t.values()))))
print time.time() - start        

