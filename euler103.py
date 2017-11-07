import time
import itertools
import math

start = time.time()
p = {}
n = 7
seed = []
sa = [[18,19,20,21,22],
      [29,30,31,32,33,34,35],
      [36,37,38,39,40,41,42], 
      [38,39,40,41,42,43], 
      [39,40,41,42,43,44], 
      [41,42,43,44,45,46], 
      [45,46,47,48,49,50,51,52]]
s =[]
for i0 in sa[0]:
    for i1 in sa[1]:
        for i2 in sa[2]:
            for i3 in sa[3]:
                for i4 in sa[4]:
                    for i5 in sa[5]:
                        for i6 in sa[6]:
                            if sum(i0+i1+i2+i3+i4+i5+i6) < 257 and sum(i0+i1+i2+i3+i4+i5+i6) > 254:
                                s.append([i0,i1,i2,i3,i4,i5,i6]) 

sums = s 
'''
s = range(17,52)
sums = [i for i in itertools.combinations(s,n) if sum(i) == 258]
'''   
#sums = [i for i in itertools.combinations(s,n)]
#print sums
for i in sums:
    a = []
    for j in range(1,len(i)):    
        for k in itertools.combinations(i,j):
            a.append(k)
    b = set([sum(x) for x in a])
    #print i
    #print a
    #print b
    if len(b) != len(a):
        continue
    b = {}
    for x in range(1,n):
        b[x] = []
        for y in a:
            if len(y) == x:
                b[x].append(y)
    ok = True
    b.keys().pop()
    for x in b.keys():
        for y in b[x]:
            for z in range(x+1,n):
                for c in b[z]:
                    if sum(y) > sum(c):
                        ok = False
                if not ok:
                    break
            if not ok:
                break
        if not ok:
            break
    if ok:
        st = ''
        for x in list(i):
            st = st + str(x)
        print i, sum(i), st
                       
    #print b
    #print a

'''
    test = True
    for k in range(1,len(a)):
        for j in itertools.combinations(a,k):
            b = set(j)
            c = a - b
            #print a,b,c
            for l in range(1,len(c)+1):
                for d in itertools.combinations(c,l):
                    
                    if sum(list(d)) == sum(list(b)): 
                        test = False
                        break
                    if len(b) > len(d) and sum(list(b)) < sum(list(d)):
                        test = False 
                        break
                    if len(d) > len(b) and sum(list(d)) < sum(list(b)):
                        test = False   
                        break
    if test:
        p[i] = a
       
print p[min(p.keys())]
'''
print(time.time() - start)        

