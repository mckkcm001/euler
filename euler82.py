import time
from itertools import chain
start = time.clock()

with open('matrix.txt','r') as f:
    b = [[int(i) for i in r.split(',')] for r in f.readlines()]
'''
b = [
    [131,673,234,103,18],
    [201,96,342,965,150],
    [630,803,746,422,111],
    [537,699,497,121,956],
    [805,732,524,37,331]
    ]
'''  
n = len(b)
a = {}
for i in range(n): 
    for j in range(n):
        a[i,j] = b[i][j]
        
s = []
for i in range(n):
    inc = a.copy()
    fro = {}
    exc = {}
    selpt = (i,0)
    exc[selpt] = inc[selpt]
    fmin = inc[selpt]
    fminpt = selpt
    del inc[selpt]
    
    def add_fro():
        global fmin,fminpt
        if selpt[0] > 0 and (selpt[0]-1,selpt[1]) in inc:         
            fro[selpt[0]-1,selpt[1]]=inc[selpt[0]-1,selpt[1]]+exc[selpt]
            del inc[selpt[0]-1,selpt[1]]
                
        if selpt[0] < n-1 and (selpt[0]+1,selpt[1]) in inc:         
            fro[selpt[0]+1,selpt[1]]=inc[selpt[0]+1,selpt[1]]+exc[selpt]
            del inc[selpt[0]+1,selpt[1]]
                
        if selpt[1] < n-1 and (selpt[0],selpt[1]+1) in inc:         
            fro[selpt[0],selpt[1]+1]=inc[selpt[0],selpt[1]+1]+exc[selpt]
            del inc[selpt[0],selpt[1]+1]
    '''        
        if selpt[1] > 0 and (selpt[0],selpt[1]-1) in inc:         
            fro[selpt[0],selpt[1]-1]=inc[selpt[0],selpt[1]-1]+exc[selpt]
            del inc[selpt[0],selpt[1]-1]
    '''
    def new_selpt():
        global selpt    
        selpt = min(fro.items(), key = lambda x: x[1])[0]
        exc[selpt] = fro[selpt]
        del fro[selpt]
        
    while selpt[1] < n-1:
        add_fro()
        #print fro
        new_selpt()
       #print selpt, exc[selpt]
        #print exc
            
    s.append(exc[selpt])
print min(s)
print(time.clock() - start)
