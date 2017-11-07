import time
import math
import random

start = time.time()

levels = {}
levels[1] = {(1,1,1,1):1}

def process(lev):
    levels[lev+1]={}
    for i in levels[lev]:
        for j in range(4):
            new = list(i)
            if new[j] != 0:
                new[j] -= 1
                for k in range(j+1,4):
                    new[k] += 1
                new = tuple(new)
                #print new
                
                if new in levels[lev+1]:
                    levels[lev+1][new] += (new[j]+1)*levels[lev][i]
                else:
                    levels[lev+1][new] = (new[j]+1)*levels[lev][i]
                
c = 0                
for i in range(1,15):        
    process(i)
    for j in levels[i+1]:
        #print i,j,sum(j)
        if sum(j) == 1:
            c += levels[i+1][j]
            
print i,1.*c/sum(levels[i].values())
print levels[15]
print time.time() - start        
