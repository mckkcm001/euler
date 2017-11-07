import time
start = time.clock()
import matplotlib.pyplot as plt
import pickle

def make_set(n):
    s = set([(0,0),(n,n)])
    r = 2*n
    p=0
    print('starting '+str(n))
    while p <= r:
        if p%1000000 == 0: print(p,time.clock() - start)
        x = pow(2,p,n)
        y = pow(3,p,n)
        s.add((x,y))
        p += 1        
    return s

def make_file(n):
    s=open('euler411set'+str(n)+'.txt','w')
    s.writelines('0','0')
    r = 2*n**5
    p=0
    print('starting '+str(n))
    while p <= r:
        if p%1000000 == 0: print(p,time.clock() - start)
        x = pow(2,p,n)
        y = pow(3,p,n)
        s.write(str(x)+','+str(y)+'\n')
        p += 1  
    
    s.close()
    
def plot_data(a,n):  
    x=[]
    y=[]
    for i,j in a:
      x.append(i)
      y.append(j) 
    plt.scatter(x,y)    
    plt.xlim([0,n])
    plt.ylim([0,n])

make_file(1)
    
'''    
for k in range(29,30):
    n = k**5
    s = make_set(n)
    pickle.dump(s,open('euler411set'+str(k)+'.pkl','wb'))
'''
print(time.clock() - start)