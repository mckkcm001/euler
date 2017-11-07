import time
import itertools
import math
start = time.time()

p = [2,3,5,7,11,13,17,19,23,29,31,37]
n = 1 
a=[1]
pf = [2,2,2,2,3,3,3,3,3,3,5,5,5,5,7,7,11,11,13,13,17,17,19,19,23,23,29,29]
t = 0
for i in range(len(pf)):
    t += len(set(itertools.combinations(pf,i)))
prod = 1
for i in range(0,len(pf),2):
    prod *= pf[i]
print t/2+1,prod


           
print(time.time() - start)
        

