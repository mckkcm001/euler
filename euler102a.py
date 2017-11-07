import time
import math
import matplotlib.pylab as plt
start = time.time()

def tri(x):
    x1 = int(x[0])*1.
    y1 = int(x[1])*1.
    x2 = int(x[2])*1.
    y2 = int(x[3])*1.
    x3 = int(x[4])*1.
    y3 = int(x[5])*1.
    if x1 == x2:
        y12 = None
    elif x1 < 0 and x2 > 0:
        y12 = y1 - (y2 - y1) / (x2 - x1) * x1
    elif x1 > 0 and x2 < 0:
        y12 = y2 - (y2 - y1) / (x2 - x1) * x2
    else:
        y12 = None
    if x1 == x3:
        y13 = None    
    elif x1 < 0 and x3 > 0:
        y13 = y1 - (y3 - y1) / (x3 - x1) * x1
    elif x1 > 0 and x3 < 0:
        y13 = y3 - (y3 - y1) / (x3 - x1) * x3
    else:
        y13 = None
    if x3 == x2:
        y23 = None
    elif x2 < 0 and x3 > 0:
        y23 = y2 - (y3 - y2) / (x3 - x2) * x2
    elif x2 > 0 and x3 < 0:
        y23 = y3 - (y3 - y2) / (x3 - x2) * x3
    else:
        y23 = None
    
    if y1 == y2:
        x12 = None
    elif y1 < 0 and y2 > 0:
        x12 = x1 - (x2 - x1) / (y2 - y1) * y1
    elif y1 > 0 and y2 < 0:
        x12 = x2 - (x2 - x1) / (y2 - y1) * y2
    else:
        x12 = None
    if y1 == y3:
        x13 = None
    elif y1 < 0 and y3 > 0:
        x13 = x1 - (x3 - x1) / (y3 - y1) * y1
    elif y1 > 0 and y3 < 0:
        x13 = x3 - (x3 - x1) / (y3 - y1) * y3
    else:
        x13 = None
    if y3 == y2:
        x23 = None
    elif y2 < 0 and y3 > 0:
        x23 = x2 - (x3 - x2) / (y3 - y2) * y2
    elif y2 > 0 and y3 < 0:
        x23 = x3 - (x3 - x2) / (y3 - y2) * y3
    else:
        x23 = None
    if (min([x12,x13,x23]) <= 0 and
        max([x12,x13,x23]) >= 0 and
        min([y12,y13,y23]) <= 0 and
        max([y12,y13,y23]) >= 0 ):
            print 'in center'
    print x
    print (x12,y12),(x13,y13),(x23,y23)    
    s1x = [x1,x2,x3,x1]
    s1y = [y1,y2,y3,y1]
    s2x = [x1,x2,x3,0]
    s2y = [y1,y2,y3,0]
    s3x = []
    s3y = []
    for i in range(3):
        if x12:
            s3x.append(x12)
            s3y.append(0)
        if x13:
            s3x.append(x13)
            s3y.append(0)
        if x23:
            s3x.append(x23)
            s3y.append(0)
        if y12:
            s3y.append(y12)
            s3x.append(0)
        if y13:
            s3y.append(y13)
            s3x.append(0)
        if y23:
            s3y.append(y23)
            s3x.append(0)
    plt.plot(s1x,s1y, c='r')

    plt.scatter(s2x,s2y, color='b',s=20)
    plt.scatter(s3x,s3y, color='b',s=20)

    plt.xlim(-1000,1000)
    plt.ylim(-1000,1000)
    plt.show()
    
#tri(['-340', '495', '-153', '-910', '835', '-947'])       
tri( ['448', '617', '-988', '0', '-103', '-504'])     
print(time.time() - start)        

