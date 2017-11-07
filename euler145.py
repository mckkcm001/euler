import time
start = time.time()

def reversible(n):
    return str(n)[::-1]

def odds(n):
    for i in str(n):
        if int( i)%2 == 0:
            return False
    return True

c = 0
for i in range(1000):
    print "i = "+str(i)
    for j in range(1000):
        for k in range(1000):
            n = k + 1000*j+1000*1000*i
            if reversible(n)[0] == '0':
                continue
            if  odds(n + int(reversible(n))):
                c+=1    
print c
    
print(time.time() - start)     
