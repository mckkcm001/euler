import bisect
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
        #if p%1000000 == 0: print(p)
        x = pow(2,p,n)
        y = pow(3,p,n)
        s.add((x,y))
        p += 1        
    return s
    
n = 6**5

s = make_set(n)

sx = sorted(s,key=lambda i: (i[0], i[1]) )
sy = sorted(s,key=lambda i: (i[1], i[0]) )
x = sorted(set([i[0] for i in sx]))
y = sorted(set([i[1] for i in sy]))

#print x
#print y
dx = {}
for i in sx:
    try:
        dx[i[0]].append(i[1])    
    except:       
        dx[i[0]] = [i[1]]

dy = {}        
for i in sy:
    try:
        dy[i[1]].append(i[0])
    except:
       dy[i[1]] = [i[0]]
#print dx
#print dy

px=[]
py=[]
'''                      
for k in s:
    px.append(k[0])
    py.append(k[1])
'''    
for j in y:
    for k in dy[j]:
        px.append(k)
        py.append(j)
    
plt.scatter(px,py, color='blue',s=20)
#plt.plot(s4x,s4y, c='r')
#plt.scatter(s3x,s3y, color='g',s=20)
#plt.scatter(s1x,s1y, color='red',s=20)
#plt.scatter(s4x,s4y, color='black',s=20)

#plt.plot(s2x,s2y, c='b')
#plt.plot(s3x,s3y, c='g')

plt.xlim(0,n)
plt.ylim(0,n)
plt.show()

def getFrontier(p):
    a = set()
    ymax = n+1
    xmax = n+1
    xi = iter(x[bisect.bisect_left(x,p[0]):])
    yj = iter(y[bisect.bisect_left(y,p[1]):])
    xmin = xi.next()
    ymin = yj.next()
    
    pos = bisect.bisect_right(dx[xmin],ymin)
    if pos < len(dx[xmin]):
        yg = dx[xmin][pos]
        if yg < ymax:
            ymax = yg
            #print("New ymax = {0}".format(ymax))
            a.add((p[0],ymax))
            #print( "Adding ({0}, {1})".format(xmin,ymax))

    pos = bisect.bisect_right(dy[ymin],xmin)
    if pos < len(dy[ymin]):
        xg = dy[ymin][pos]
        if xg < xmax:
            xmax = xg
            #print("New xmax = {0}".format(xmax))
            a.add((xmax,ymin))
            #print( "Adding ({0}, {1})".format(xmax,ymin))        
    
    xdone = False
    ydone = False    
    while not xdone or not ydone:
        try:
            xmin=xi.next()
            pos = bisect.bisect_left(dx[xmin],ymin)
            if pos < len(dx[xmin]):
                yg = dx[xmin][pos]
                if yg < ymax:
                    ymax = yg
                    #print("New ymax = {0}".format(ymax))
                    a.add((xmin,ymax))
                    #print( "Adding ({0}, {1})".format(xmin,ymax))
        except:
            xdone = True
        
        try:
            ymin=yj.next()
            pos = bisect.bisect_left(dy[ymin],xmin)
            if pos < len(dy[ymin]):
                xg = dy[ymin][pos]
                if xg < xmax:
                    xmax = xg
                    #print("New xmax = {0}".format(xmax))
                    a.add((xmax,ymin))
                    #print( "Adding ({0}, {1})".format(xmax,ymin))
        except:
            ydone = True
        
    return a

#print('x = {0}'.format(x))      
#print('y = {0}'.format(y))  
#print('dx[0] = {0}'.format(dx[0]))      
#print('dy[0] = {0}'.format(dy[0]))
#print('dx[1] = {0}'.format(dx[1]))      
#print('dy[1] = {0}'.format(dy[1]))

def reduceFrontier(g):
    gx = sorted(g,key=lambda i: (i[0], i[1]) )
    h = set()
    h.add((gx[0][0],gx[0][1]))
    xmin = gx[0][0]
    ymax = gx[0][1]
    for i in range(1,len(gx)):
        if gx[i][1] <  ymax and gx[i][0] > xmin:
            h.add((gx[i][0],gx[i][1]))
            ymax = gx[i][1] 
            xmin = gx[i][0] 
    return h
    
f=set()
f.add((0,0))
count = 0
stop = set()
stop.add((n,n))
while(f != stop):
    count += 1
    g = set()
    s1x=[]
    s1y=[]
    for i in f:
        g = g.union(getFrontier(i))
        s1x.append(i[0])
        s1y.append(i[1])
        #print count, i
    #print g
    f = reduceFrontier(g)
    #print f
    plt.scatter(s1x,s1y, color=str(count/110.),s=20)
    
        
print count - 1
print time.clock()-start
