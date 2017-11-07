import operator
import math
import time
start = time.time()

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n == 3: return True
    if n%2 == 0:
        return False
    for i in range(3,int(n**.5) + 1,2):
        if n%i == 0: return False
    return True
    
rings = 1500
d = {(0,0):1}
count = 1
y = 0
for i in range(rings):
    x = 0
    y += 1
    for j in range(i+1):  
        count += 1
        d[(x,y)] = count
        #print (x,y), d[(x,y)]        
        if x%2 == 0:
            y -= 1
        x -= 1
    for j in range(i+1):  
        count += 1
        d[(x,y)] = count
        # print (x,y), d[(x,y)]
        y -= 1
    for j in range(i+1):  
        count += 1
        d[(x,y)] = count
        #print (x,y), d[(x,y)]
        if x%2 == 0:
            y -= 1
        x += 1
    for j in range(i+1):  
        count += 1
        d[(x,y)] = count
        #print (x,y), d[(x,y)]
        x += 1
        if x%2 == 0:
            y += 1
        
    for j in range(i+1):  
        count += 1
        d[(x,y)] = count
        #print (x,y), d[(x,y)]
        y += 1
    for j in range(i+1):  
        count += 1
        d[(x,y)] = count
        #print (x,y), d[(x,y)]
        x -= 1
        if x%2 == 0:
            y += 1
        
print ('Count = ' + str(count))
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
#print sorted_d
a = []
for i in sorted_d:
    #print i
    np = 0
    pt = i[0]
    x = pt[0]
    y = pt[1]
    if x%2 == 0:
        try:
            if is_prime(abs(d[(x,y+1)] - d[(x,y)])): np+=1
            if is_prime(abs(d[(x+1,y)] - d[(x,y)])): np+=1
            if is_prime(abs(d[(x+1,y-1)] - d[(x,y)])): np+=1
            if is_prime(abs(d[(x,y-1)] - d[(x,y)])): np+=1
            if is_prime(abs(d[(x-1,y-1)] - d[(x,y)])): np+=1
            if is_prime(abs(d[(x-1,y)] - d[(x,y)])): np+=1 
            #print d[(x,y+1)]
            #print d[(x-1,y)],d[(x,y)],d[(x+1,y)]
            #print d[(x-1,y-1)],d[(x,y-1)],d[(x+1,y-1)]
            if np == 3:
                a.append(d[(x,y)])
        except:
            break
    else:
        try:
            if is_prime(abs(d[(x,y+1)] - d[(x,y)])): np+=1
            if is_prime(abs(d[(x+1,y+1)] - d[(x,y)])): np+=1
            if is_prime(abs(d[(x+1,y)] - d[(x,y)])): np+=1
            if is_prime(abs(d[(x,y-1)] - d[(x,y)])): np+=1
            if is_prime(abs(d[(x-1,y)] - d[(x,y)])): np+=1
            if is_prime(abs(d[(x-1,y+1)] - d[(x,y)])): np+=1 
            #print d[(x,y+1)]
            #print d[(x-1,y+1)],d[(x,y)],d[(x+1,y+1)]
            #print d[(x-1,y)],d[(x,y-1)],d[(x+1,y)]
            if np == 3:
                a.append(d[(x,y)])
        except:
            break
print (len(a))
print(time.time() - start )       
