import time
start = time.clock()
import pickle
from operator import itemgetter
import matplotlib.pylab as plt
import re 

'''
k = 22
n = k**5
a = list(pickle.load( open( 'euler411set'+str(k)+'.pkl', "rb" ) ))    
sx=[]
sy=[]
for i in a:
    if i[0] > i[1] : sx.append(i)
    else: sy.append(i)

sx = sorted(sx,key=itemgetter(0,1))
sy = sorted(sy,key=itemgetter(1,0))
'''

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
    
n = 10000
s=list(make_set(n))

print 'after making set'
print(time.clock() - start)

#print 'the set of points'
#print s
ss = list(s)
fro = []
path = []
path.append((0,0))

if (1,0) in s:
    fro.append((1,0))
    s.remove((1,0))
if (0,1) in s:
    fro.append((0,1))
    s.remove((0,1))
if len(fro) == 0:
    fro.append((1,1))
    s.remove((1,1))
    
#print 'frontier and set at 1,1'
#print fro
#print s

selpt = min([i for i in fro])
#print 'select minimum distance point around 1,1'
#print selpt

if len(fro) == 1:
    path.append((1,1))
    fro.remove((1,1))
#    print 'delete 1,1 from frontier and add to path'
#    print fro
#    print path

print 'after setup'
print(time.clock() - start) 
   
def add_fro():
    global selpt
    d=1
    done = False
    while not done and d <= n:
        pts = [(d-i + selpt[0], i + selpt[1]) for i in range(d+1)]
#        print 'points to test for nearest point'
#        print pts
        for i in pts:
            if i in s:
                fro.append(i)
                s.remove(i)
                selpt = i
                done = True
                break
        d+=1
    #print 'frontier after finding least distant point'
    #print fro
    
    f = [i for i in s if i[1] < selpt[1] or i[0] < selpt[0]]
    for i in f:
        fro.append(i)
        s.remove(i)
        
    #print 'frontier after adding points outside least distant point'
    #print fro

def new_selpt():
    global selpt  
    # pick point that excludes the least other points
    exc = {}    
    for i in fro:
        pts = 0
        for j in s:
            if i[0] > j[0] or i[1] > j[1]:
                pts += 1
        for j in fro:
            if i[0] > j[0] or i[1] > j[1]:
                pts += 1
        exc[i]=pts
        
    selpt = min(exc.items(), key = lambda x: x[1])[0]
    #print 'find point on frontier that excludes least other points'
    #print selpt 
   # print exc
    path.append(selpt)        
    for i in exc:
        if i == selpt: continue
        if selpt[0] <= i[0] and selpt[1] <= i[1]:
           # print 'add value back into s'
           # print i
            s.append(i)
    f = [i for i in s if i[1] < selpt[1] or i[0] < selpt[0]]
    for i in f:
        s.remove(i)        
            
    fro[:] = []

while (n,n) not in path:    
    add_fro() 
    print 'after add_fro'
    print(time.clock() - start)
    new_selpt()
    print 'after selpt'
    print(time.clock() - start)

        
s1x = [i[0] for i in s]
s1y = [i[1] for i in s]
s2x = [i[0] for i in ss]
s2y = [i[1] for i in ss]
s3x = [i[0] for i in fro]
s3y = [i[1] for i in fro]
s4x = [i[0] for i in path]
s4y = [i[1] for i in path]

plt.scatter(s2x,s2y, color='yellow',s=4)
plt.plot(s4x,s4y, c='r')
plt.scatter(s3x,s3y, color='g',s=20)
plt.scatter(s1x,s1y, color='b',s=20)
plt.scatter(s4x,s4y, color='black',s=20)

#plt.plot(s2x,s2y, c='b')
#plt.plot(s3x,s3y, c='g')

plt.xlim(0,n)
plt.ylim(0,n)
plt.show()
print(len(path)-2)   
print(time.clock() - start)
