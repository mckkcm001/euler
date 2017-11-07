import time
start = time.time()

n = 50
red=[1,1,2,4,8,15]
for i in range(6,n+1):
    red.append(red[i-1]+red[i-2]+red[i-3]+red[i-4])
print red[n]



print time.time() - start