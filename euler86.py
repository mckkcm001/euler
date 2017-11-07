import time
import random
import operator

start = time.clock()

def get_path1(a,b,c):
    pt = a*b/(a+c)
    s1 = (a**2 + pt**2)**.5
    s2 = (c**2 + (b-pt)**2)**.5
    return s1 + s2
    
def get_path2(a,b,c):
    if a == c: return m*3
    pt = a*b/(a-c)
    s1 = (a**2 + pt**2)**.5
    s2 = (c**2 + (b-pt)**2)**.5
    return s1 + s2

m = 10
tot = 0
for a in range(1,m):
    for b in range(1,m):
        for c in range(1,m):
            p1 = get_path1(a,b,c)
            p2 = get_path1(b,c,a)
            p3 = get_path1(c,a,b)
            pmin = min([p1,p2,p3])
            if  pmin == int(pmin):
                print a,b,c
                print p1,p2,p3,pmin
                tot += 1
            p1 = get_path2(a,b,c)
            p2 = get_path2(b,c,a)
            p3 = get_path2(c,a,b)
            pmin = min([p1,p2,p3])
            if pmin < m*3 and pmin == int(pmin):
                print a,b,c
                print p1,p2,p3,pmin
                tot += 1
print tot 
print(time.clock() - start)
