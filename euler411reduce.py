import time
start = time.clock()
import pickle
from operator import itemgetter
import matplotlib.pylab as plt
import re 
import sys
from pprint import pprint

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
    
n = 2**5
s = sorted(make_set(n))

sx = sorted(set([i[0] for i in s]))
sy = sorted(set([i[1] for i in s]))
'''
a = [[0 for i in range(len(sx))] for i in range(len(sy))]

for i in s:
    a[sy.index(i[1])][sx.index(i[0])]=1
'''
s1x=[]
s1y=[]
s2x=[]
s2y=[]                       
for i in range(len(sy)):
    for j in range(len(sx)):
        if (sx[j],sy[i]) in s:
            s1y.append(i)
            s1x.append(j)

#plt.scatter(s2x,s2y, color='black',s=10)
#plt.plot(s4x,s4y, c='r')
#plt.scatter(s3x,s3y, color='g',s=20)
plt.scatter(s1x,s1y, color='red',s=20)
#plt.scatter(s4x,s4y, color='black',s=20)

#plt.plot(s2x,s2y, c='b')
#plt.plot(s3x,s3y, c='g')

plt.xlim(0,len(sx)-1)
plt.ylim(0,len(sy)-1)
plt.show()

'''
print 'dx done'
pprint(dx)
print 'dy done'
pprint(dy)
print 'dd done'
pprint(dd)
''' 
'''      
print 'after making lists'
print(time.clock() - start)

def proc_row(d):
    if d in dx.keys():
        xval = sorted(dx[d].keys())
        tot = dd[d][d][1]
        for i in xval:
            #print 'in proc row ' + str(d)
            #print dx[d][i][1],tot,dx[d][i][0]
            dx[d][i][1] = max(tot+dx[d][i][0],dx[d][i][1])
            tot = dx[d][i][1]
            #print 'in proc row ' + str(d)
            #print dx[d][i][1],tot,dx[d][i][0]

def proc_col(d):
    if d in dy.keys():
        yval = sorted(dy[d].keys())
        tot = dd[d][d][1]
        for i in yval:
            dy[d][i][1] = max(tot + dy[d][i][0],dy[d][i][1])
            tot = dy[d][i][1]

def next_dia(d):
     nd = sd[sd.index(d) + 1]
     dd[nd][nd][1]=dd[d][d][1]+dd[nd][nd][0]   
     
def next_row(d):
    nd = sd[sd.index(d) + 1]
    try:
        nx = sx[sx.index(d) + 1]
    except:
        nx = n
    xval = sorted(dx[d].keys())
    #print 'in next row ' + str(d)
    #print nx, xval,d,dx[d]
    for i in xval:
        if i <= nd:
            dd[nd][nd][1] = max(dx[d][i][1], dd[d][d][1]) + dd[nd][nd][0]
        else:
            if i > nx:
                if i in dx[nx].keys():
                    dx[nx][i][1] = dx[d][i][1] + dx[nx][i][0]
                else:
                    dx[nx].update({i:[0,dx[d][i][1]]})

def next_col(d):
    nd = sd[sd.index(d) + 1]
    try:
        ny = sy[sy.index(d) + 1]
    except:
        ny = n
    yval = sorted(dy[d].keys())
    #print 'in next col' + str(d)
    #print ny, yval,d,dy[d]
    for i in yval:
        if i <= nd:
            dd[nd][nd][1] = max(dy[d][i][1], dd[d][d][1]) + dd[nd][nd][0]
           # print 'eval of next col'
            #print dd[nd][nd][1], dy[d][i][1], dd[d][d][1], dd[nd][nd][0]
        else:
            if i > ny:
                if i in dy[ny].keys():
                    dy[ny][i][1] = dy[d][i][1] + dy[ny][i][0]
                else:
                    dy[ny].update({i:[0,dy[d][i][1]]})     


for i in sd[0:-1]:
    if i in dx.keys():
        #print 'call proc row' + str(i)
        proc_row(i)
       # print 'dx done'
     #   pprint(dx)
        
    if i in dy.keys():
       # print 'call proc col' + str(i)
        proc_col(i)
       # print 'dy done'
    #    pprint(dy)
        
    next_dia(i)
   # print 'dd done'
  #  pprint(dd)
    
    if i in dx.keys():
        next_row(i)
      #  print 'call next row' + str(i)
       # print 'dx done'
       # pprint(dx)
        
    if i in dy.keys():
      #  print 'call next col' + str(i)
        next_col(i)
      #  print 'dy done'
       # pprint(dy)
'''        
   
'''    
if sd[-2] in dx.keys():
    for i in dx[sd[-2]]:
        dd[n][n][1] = max(dx[sd[-2]][i][1]+dd[n][n][0],dd[n][n][1])
if sd[-2] in dy.keys():
    for i in dy[sd[-2]]:
        dd[n][n][1] = max(dy[sd[-2]][i][1]+dd[n][n][0],dd[n][n][1])
'''    
print 'after processing'
print(time.clock() - start)
'''                       
s1x=[]
s1y=[]                       
for k in dy:
    for v in dy[k]:
        s1x.append(k)
        s1y.append(v)
for k in dx:
    for v in dx[k]:
        s1y.append(k)
        s1x.append(v)
for k in dd:
    for v in dd[k]:
        if dd[k][v][0] != 0:
            s1y.append(k)
            s1x.append(v)

#plt.scatter(s2x,s2y, color='red',s=20)
#plt.plot(s4x,s4y, c='r')
#plt.scatter(s3x,s3y, color='g',s=20)
plt.scatter(s1x,s1y, color='blue',s=5)
#plt.scatter(s4x,s4y, color='black',s=20)

#plt.plot(s2x,s2y, c='b')
#plt.plot(s3x,s3y, c='g')

plt.xlim(0,n)
plt.ylim(0,n)
plt.show()

print dd[n]   
'''
print(time.clock() - start)
