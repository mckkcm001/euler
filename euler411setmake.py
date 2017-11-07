import matplotlib.pylab as plt
from operator import itemgetter

def make_set(n):
    s = set([(n,n)])
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

def get_fpt(x,y):
    done = False
    t = 1
    while not done:      
        for i in range(t+1):
            if (x+i,y+t) in s:
                return (x+i,y+t)
            if (x+t,y+i) in s:
                return (x+t,y+i)
        if x+t>=n or y+t>=n: return (n,n)
        t+=1

def get_loss(p):
    count = 0
    for i in sx:
        if i[0] >= p[0]: break
        count+=1
    for i in sy:
        if i[1] >= p[1]: break
        count+=1
    return count

def get_pts(p):
    h=set()
    for i in sx:
        if i[0] >= p[0]: break
        h.add(i)
    for i in sy:
        if i[1] >= p[1]: break
        h.add(i)
    return h
   
k=30
n = 22
s = make_set(n)
print s
f = [(0,0)]
g = (0,0)
while g != (n,n):
    sx = sorted(s,key=itemgetter(0,1))
    sy = sorted(s,key=itemgetter(1,0))
    
    g = get_fpt(g[0],g[1]) 
    h = get_pts(g)
    
    min = len(h)
    for i in h:
        if get_loss(i) < min:
            g = i
            
    f.append(g)
    s.difference(h)
    s.remove(g)    


fx = [i[0] for i in f]
fy = [i[1] for i in f]
sx = [i[0] for i in s]
sy = [i[1] for i in s]
print sx
#plt.plot(fx,fy)
plt.scatter(fx,fy, s=5)
plt.xlim(0,n)
plt.ylim(0,n)
plt.show()
print(len(f)-2)