import time
start = time.time()

import numpy as np

def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        for i in m:
            yield i
        m = np.dot(m, uad)

def gen_all_pyth_trips(limit):
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim
            
n=0
pt=[]
for i in gen_all_pyth_trips(50000000):
    if i[0]+i[1]+i[2] < 100000000:
        if i[0] < i[1] and i[2]%(i[1]-i[0])==0:
            n+=1
        elif i[2]%(i[0]-i[1])==0:
            n+=1
        
print n            
print time.time() - start