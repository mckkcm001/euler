import time
start = time.clock()

def sqroot(a, digits):
    a = a * (10**(2*digits))
    x_prev = 0
    x_next = 1 * (10**digits)
    while x_prev != x_next:
        x_prev = x_next
        x_next = (x_prev + (a // x_prev)) >> 1
    return x_next
s=0
for i in range(2,100):
    if int(i**.5) == i**.5:
        print i
        continue
    nbr = str(sqroot(i,99))
    print i,nbr[0:4], i**.5
    for j in nbr:
        s += int(j)  
print s          

print(time.clock() - start)
