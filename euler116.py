import time
start = time.time()

n = 50
red=[1,1,2]
for i in range(3,n+1):
    red.append(red[i-1]+red[i-2])
print red[n]-1

green=[1,1,1,2,3]
for i in range(5,n+1):
    green.append(green[i-1]+green[i-3])
print green[n]-1

blue=[1,1,1,1,2,3]
for i in range(6,n+1):
    blue.append(blue[i-1]+blue[i-4])
print blue[n]-1

print red[n]-1+green[n]-1+blue[n]-1

print time.time() - start