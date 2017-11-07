import matplotlib.pyplot as plt
import sys
import time
start = time.clock()

'''
k = 28
n = k**5
s = list(pickle.load( open( 'euler411set'+str(k)+'.pkl', "rb" ) ))    
print 'list loaded'
'''

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
    
n = 123 #2**5
s = make_set(n)

dx = {0:{0:[1,(0,0)]},n:{n:[1,(0,0)]},1:{1:[1,(0,0)]}}
dy = {0:{0:[1,(0,0)]},n:{n:[1,(0,0)]},1:{1:[1,(0,0)]}}
sx = [0,1,n]
sy = [0,1,n]
F = set()
goal = [1,(0,0)]
for i in s:
    if i[0] < i[1]:
        try:
            dy[i[0]].update({i[1]:[1,(0,0)]})
        except:
            dy[i[0]]={}
            dy[i[0]].update({i[1]:[1,(0,0)]})
            sx.append(i[0])
    if i[0] > i[1]:
        try:
            dx[i[1]].update({i[0]:[1,(0,0)]})
        except:
            dx[i[1]]={}
            dx[i[1]].update({i[0]:[1,(0,0)]}) 
            sy.append(i[1])
        
sx.sort()
sy.sort()

s1x=[]
s1y=[]
s2x=[]
s2y=[]                       
for k in dy:
    for v in dy[k]:
        s1x.append(k)
        s1y.append(v)
s1x.append(1)
s1y.append(1)
for k in dx:
    for v in dx[k]:
        s2y.append(k)
        s2x.append(v)

plt.scatter(s2x,s2y, color='blue',s=20)
#plt.plot(s4x,s4y, c='r')
#plt.scatter(s3x,s3y, color='g',s=20)
plt.scatter(s1x,s1y, color='red',s=20)
#plt.scatter(s4x,s4y, color='black',s=20)

#plt.plot(s2x,s2y, c='b')
#plt.plot(s3x,s3y, c='g')

plt.xlim(0,n)
plt.ylim(0,n)
plt.show()

try:
    x = sorted(dx[0])
    for i in range(1,len(x)):
        dx[0][x[i]][0] = dx[0][x[i-1]][0] + 1       
        dx[0][x[i]][1] = (x[i-1],0)
    if x[-1] > 0:
        F.add((x[-1],0))        
except:
    pass

try:
    y = sorted(dy[0])
    for i in range(1,len(y)):
        dy[0][y[i]][0] = dy[0][y[i-1]][0] + 1       
        dy[0][y[i]][1] = (0,y[i-1])
    if y[-1] > 0:
        F.add((0,y[-1]))
except:
    pass
  
F.add((1,1))

def proc_dx(x,y,v):
    max_x = n+1
    pn = (x,y)
    while y < n:
        print 'while y < n'
        print y,n
        try:
            new_x = min([i for i in dx[y] if i > x])
            new_v = dx[y][new_x][0]
            print 'new_x, new_v'
            print new_x, new_v
            if new_x < max_x:
                max_x = new_x
                print 'set max_x to new_x'
                print max_x, new_x
                if new_v < v + 1:
                    dx[y][new_x][0] = v + 1
                    dx[y][new_x][1] = pn
                    print 'dx[y][new_x][0], dx[y][new_x][1]'
                    print dx[y][new_x][0], dx[y][new_x][1]
                F.add((new_x,y))
                print 'F'
                print F
        except:
            pass

        y = sy[sy.index(y)+1]
        print 'update y'
        print y
                                 
    if y == n:
        print 'y==n'
        f = dx[pn[1]][x]
        print 'pn[1], x, dx[pn[1]][x]'
        print pn[1], x, dx[pn[1]][x]
        if f[0] + 1 > goal[0]:
            goal[0] = f[0]+1
            goal[1] = pn
        print ' update goal'
        print goal
        return
        
    if max_x > x:
        max_y = n+1
        while x < max_x:
            try:
                new_y = min(dy[x])
                new_v = dy[x][new_y][0]
                if new_y < max_y:
                    max_y = new_y
                    if new_v < v + 1:
                        dy[x][new_y][0] = v + 1
                        dy[x][new_y][1] = pn
                    F.add((x,new_y))
            except:
                pass
            x = sx[sx.index(x)+1]

def proc_dy(x,y,v):
    max_y = n+1
    pn = (x,y)
    while x < n:
        print 'while x < n'
        print x,n
        try:
            new_y = min([i for i in dy[x] if i > y])
            new_v = dy[x][new_y][0]
            print 'new_y, new_v'
            print new_y, new_v
            if new_y < max_y:
                max_y = new_y
                print 'set max_y to new_y'
                print max_y, new_y
                if new_v < v + 1:
                    dy[x][new_y][0] = v + 1
                    dy[x][new_y][1] = pn
                    print 'dy[x][new_y][0], dy[x][new_y][1]'
                    print dy[x][new_y][0], dy[x][new_y][1]
                F.add((x,new_y))
                print 'F'
                print F
        except:
            pass

        x = sx[sx.index(y)+1]
        print 'update x'
        print x                 
                                 
    if x == n:
        f = dy[pn[0]][y]
        if f[0] + 1 > goal[0]:
            goal[0] = f[0] + 1
            goal[1] = pn
        print ' update goal'
        print goal
        return
       
    if max_y > y:
        max_x = n+1
        while y < max_y:
            try:
                new_x = min(dx[y])
                new_v = dx[y][new_x][0]
                if new_x < max_x:
                    max_x = new_x
                    if new_v < v + 1:
                        dx[y][new_x][0] = v + 1
                        dx[y][new_x][1] = pn
                    F.add((new_x,y))
            except:
                pass
            y = sy[sy.index(y)+1]
            
def get_F(x,y,v):
    print 'get_F'
    print x,y,v   
    if x >= y:
        proc_dx(x,y,v)
    else:
        proc_dy(x,y,v)
        
while len(F) > 0:
    f = F.pop()
    if f[0] > f[1]:
        v = dx[f[1]][f[0]][0]
        print 'node value from dx'
        print f, v
    elif f[0] < f[1]:
        v = dy[f[0]][f[1]][0]  
        print 'node value from dy'
        print f, v
    else:
        v = 2
        try:
            v += dx[0][1][0]
            dx[1][1][1] = (1,0)
            dy[1][1][1] = (1,0)
        except:
            pass
        try:
            v += dy[0][1][0]
            dx[1][1][1] = (0,1)
            dy[1][1][1] = (0,1)
        except:
            pass
        dx[1][1][0] = v
        dy[1][1][0] = v 
    get_F(f[0],f[1],v)

path=[(n,n)] 
np = goal[1] 
while np != (0,0):
    path.append(np)
    if np[0] >= np[1]:
        np = dx[np[1]][np[0]][1]
    else:
        np = dy[np[0]][np[1]][1]
path.append((0,0))

s4x=[]
s4y=[]
for k in path:
        s4x.append(k[0])
        s4y.append(k[1])

plt.plot(s4x,s4y, c='r')

