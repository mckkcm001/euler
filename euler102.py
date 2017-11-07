import time
import math
start = time.time()

c = 0
for line in open('triangles.txt', 'r'): 
    x = line.split(',')
    x[5]= x[5].replace('\n','')
    x1 = int(x[0])*1.
    y1 = int(x[1])*1.
    x2 = int(x[2])*1.
    y2 = int(x[3])*1.
    x3 = int(x[4])*1.
    y3 = int(x[5])*1.
    p123 = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    p120 = (x2 - x1) * (0 - y1) - (y2 - y1) * (0 - x1)
    p231 = (x2 - x3) * (y1 - y3) - (y2 - y3) * (x1 - x3)
    p230 = (x2 - x3) * (0 - y3) - (y2 - y3) * (0 - x3)
    p132 = (x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)
    p130 = (x3 - x1) * (0 - y1) - (y3 - y1) * (0 - x1)
    if (math.copysign(1,p123) == math.copysign(1,p120) and
        math.copysign(1,p231) == math.copysign(1,p230) and
        math.copysign(1,p132) == math.copysign(1,p130) ):
            c += 1
            
print c       
       
print(time.time() - start)        

