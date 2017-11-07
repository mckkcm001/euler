import time
start = time.clock()

a = [0,0,1,2,4]       

n=5
s=0
for i in range(1,n):
    if i >= n-i:
        s+=1
        s+=a[n-i]
        print(i,n-i,s,a[n-i])
    else:
        s+=a[n-i]
        for j in range(1,n-i):
            s-=a[j]
        print(i,n-i,s)
        
a.append(s)
         
print(a)

print(time.clock() - start)