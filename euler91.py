import time
start = time.clock()

n = 51
s = 0
for x1 in range(n):
    for y1 in range(n):
        for x2 in range(n):
            for y2 in range(n):
                if (x1 == 0 and y1 == 0 or
                    x2 == 0 and y2 == 0 or
                    x1 == x2 and y1 == y2):
                        continue
                L1 = x1**2+y1**2
                L2 = x2**2+y2**2
                L3 = (x1-x2)**2+(y1-y2)**2
                if L1 + L2 == L3 or L1 + L3 == L2 or L3 + L2 == L1:
                    s += 1
print(time.clock() - start)                
print s/2                