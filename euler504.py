from fractions import Fraction
import random
import time
import itertools
start = time.time()

d4 = {
(1,1):0.25,(1,2):0.75,(1,3):1.25,(1,4):1.75,
(2,1):0.75,(2,2):1.25,(2,3):2.75,(2,4):3.25,  
(3,1):1.25,(3,2):2.75,(3,3):3.25,(3,4):5.75, 
(4,1):1.75,(4,2):3.25,(4,3):5.75,(4,4):6.25
}  

d100={}
for i in range(1,101):
    for j in range(i,101):
        s = .25 + (i-1)*0.5
        for k in range(1,j):
            s += .5 + int(i-1.0*i*k/j)
            if int(i-1.0*i*k/j) == i-1.0*i*k/j:
                s -= 1
            
        d100[(i,j)] = s
        d100[(j,i)] = s
#print d100
       
t = 0
for s1 in range(1,101):
    for s2 in range(1,101):
        for s3 in range(1,101):
            for s4 in range(1,101):
                sq = d100[(s1,s2)]+d100[(s2,s3)]+d100[(s3,s4)]+d100[(s4,s1)]
                #print s1,s2,s3,s4,sq
                sqr = sq**.5
                if int(sqr) == sqr:
                    t+=1
                    #print t
print t

print time.time() - start