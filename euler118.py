import time
from itertools import combinations, permutations, product, chain
start = time.time()

d = [1,2,3,4,5,6,7,8,9]

def sundaram3(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)
def norepeat(n):
    for i in str(n):
        if str(i) == '0' or str(n).count(i) > 1:
            return False
    return True

def there(n1,n2):
    for i in str(n2):
        if str(n1) == i:
            return True
    return False
   
d1 = []
d2 = []
d3 = []
d4 = []
d5 = []
d6 = []
d7 = []
d8 = []

primes = sundaram3(98765432)
for i in primes: 
    if norepeat(i):
        if i < 10:
            d1.append(i)
        elif i < 100:
            d2.append(i)
        elif i < 1000:
            d3.append(i)
        elif i < 10000:
            d4.append(i)
        elif i < 100000:
            d5.append(i)
        elif i < 1000000:
            d6.append(i)
        elif i < 10000000:
            d7.append(i)
        elif i < 100000000:
            d8.append(i)

d=[d1,d2,d3,d4,d5,d6,d7,d8]
 
combos = [
[3, 3, 0, 0, 0, 0, 0, 0],
[1, 4, 0, 0, 0, 0, 0, 0],
[4, 1, 1, 0, 0, 0, 0, 0],
[2, 2, 1, 0, 0, 0, 0, 0],
[0, 3, 1, 0, 0, 0, 0, 0],
[3, 0, 2, 0, 0, 0, 0, 0],
[1, 1, 2, 0, 0, 0, 0, 0],
[0, 0, 3, 0, 0, 0, 0, 0],
[3, 1, 0, 1, 0, 0, 0, 0],
[1, 2, 0, 1, 0, 0, 0, 0],
[2, 0, 1, 1, 0, 0, 0, 0],
[0, 1, 1, 1, 0, 0, 0, 0],
[1, 0, 0, 2, 0, 0, 0, 0],
[4, 0, 0, 0, 1, 0, 0, 0],
[2, 1, 0, 0, 1, 0, 0, 0],
[0, 2, 0, 0, 1, 0, 0, 0],
[1, 0, 1, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 0],
[3, 0, 0, 0, 0, 1, 0, 0],
[1, 1, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[2, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 1, 0],
[1, 0, 0, 0, 0, 0, 0, 1]
]

p=[]

for i in combos:  
    cc=[]
    for n,j in enumerate(i):
        c=[]
        if j == 0:
            continue
        for k in combinations(d[n],j):
            s=''
            for l in k:
                s+=str(l)
            if len(set(s)) == (n+1)*j:
                c.append(k)
        cc.append(c)  
               
    for i2 in product(*cc):
        test = set(chain(*i2))
        s=""
        for j2 in test:
            s+=str(j2)
        if len(set(s)) == 9:
            p.append(test)

def make_unique(original_list):
    unique_list = []
    [unique_list.append(obj) for obj in original_list if obj not in unique_list]
    return unique_list

print len(make_unique(p))

print time.time() - start        