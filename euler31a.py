import time
start = time.clock()

n = 100

a = [i for i in range(1,n)] #array of values
c = [n//a[i-1] for i in range(1,n) if n//a[i-1] > 1 ] #starting points
b = [0 for i in range(len(c))] #counters

def add_up():
    s=0
    for i in range(n-1):
        s+=a[i]*b[i]
    return s
      
s = 0 #counter

for i in range(len(c)):
    b[i] = c[i]
    if b[i]*a[i] == n:
        s+=1
        if b[i] < 3:
            continue            
    while b[i] > 2:
        b[i] -= 1
        rem = n - a[i]*b[i]
        
d=1           
for i in c:
    d*=i
print(d)

print(time.clock() - start)                                    
