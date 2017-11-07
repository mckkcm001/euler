import time
start = time.time()

c = [1,1,1,2,4]

t = 50

for n in range(5,t+1):
    s=c[n-1]+2
    for j in range(1,n-3):
        s+=c[j]
    c.append(s)

print c
    
print time.time() - start