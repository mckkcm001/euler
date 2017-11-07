import time
start = time.clock()


s = 0
for i in range(1,10000000):
    n = i  
    while True:
        a = 0
        for j in str(n):
            a += int(j)**2
        if a == 1:
            break
        if a == 89:
            s += 1
            break       
        n = a
                
print(time.clock() - start)                
print s               