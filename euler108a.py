import time

start = time.time()

n = 2*3*5*7*11*13
s = 0
for i in range(1,n+1):
    if 1.*n*(n+i)/i == int(1.*n*(n+i)/i):
        s += 1
print s  
print(time.time() - start)        

