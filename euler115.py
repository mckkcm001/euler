import time
start = time.time()

c = []

m=50

for i in range(m):
    c.append(1)
c.append(2)
t=168
for n in range(m+1,t+1):
    s=c[n-1]+2
    for j in range(1,n-m):
        s+=c[j]
    c.append(s)

print c[-1],c[-2]
    
print time.time() - start