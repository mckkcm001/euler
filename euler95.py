import copy
import time

start = time.time()

def div_sum(n):   
    a = set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    a = list(a)
    a.remove(max(a))
    return sum(a)          

ch = []
for i in range(2,15000):
    r = []
    r.append(i)
    a = div_sum(i)
    #print i,r,a
    while True:
        r.append(a)
        if a == 1 or a == r[0]:
            break
        a = div_sum(a)
        if a in r[1:]:
            break
        if a > 1000000:
            r = []
            break
        #print r,a
    #print r    
    if r != [] and r[0] == r[-1]:
        if len(ch) < len(r):
            ch = copy.copy(r)
            print len(ch),ch

print min(ch), ch        
print(time.time() - start)        

