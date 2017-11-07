import time

start = time.time()

n = 1000000000000
d = {1:(15,21)}
k = 1
while(d[k][1] < n):
    d[k+1] = (3*d[k][0]+2*d[k][1]-2,4*d[k][0]+3*d[k][1]-3)
    k+=1

print d
print [d[i][0] for i in d if d[i][1] > n]    
print(time.time() - start)        

