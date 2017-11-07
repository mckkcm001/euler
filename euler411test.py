import matplotlib.pylab as plt
from operator import itemgetter


def make_set(n):
    s = set([(n,n),(0,0)])
    r = 2*n
    p=0
    print('starting '+str(n))
    while p <= r:
        if p%1000000 == 0: print(p)
        x = pow(2,p,n)
        y = pow(3,p,n)
        s.add((x,y))
        p += 1        
    return s
    
n = 10000
s = make_set(n)
for i in s:
    if (n-i[0],n-i[1]) not in s:
        print i
s1x=[]
s1y=[]
s2x=[]
s2y=[]                       
for k in s:
        s1x.append(k[0])
        s1y.append(k[1])


#plt.scatter(s2x,s2y, color='black',s=10)
#plt.plot(s4x,s4y, c='r')
#plt.scatter(s3x,s3y, color='g',s=20)
plt.scatter(s1x,s1y, color='red',s=20)
#plt.scatter(s4x,s4y, color='black',s=20)

#plt.plot(s2x,s2y, c='b')
#plt.plot(s3x,s3y, c='g')

plt.xlim(0,n)
plt.ylim(0,n)
plt.show()

    
