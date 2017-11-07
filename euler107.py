import time
import numpy as np
import math

def read_matrix():
    a=[]
    with open('p107_network.txt') as f:
        for line in f:
            b=[]
            s=line.strip().split(',')
            for i in s:
                if i == '-':
                    b.append(0)
                else:
                    b.append(int(i))
            a.append(b) 
    return np.array(a)
            
def remove_max(a):
    m = 0
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i][j] > m:
                x,y = i,j
                m = a[i][j]
                    
    i,j = x,y
    for k in range(len(a)):
        if k == j:
            continue
        if a[i][k] > 0 and a[j][k] > 0:
            a[i][j] = 0
            a[j][i] = 0
            return  m

    return 0

def remove_tri(a):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i][j] > 0:
                for k in range(len(a)):
                    if k == j:
                        continue
                    if a[i][k] > 0 and a[j][k] > 0:
                        if a[i][j] >= a[i][k] and a[i][j] >= a[j][k]:
                            a[i][j] = 0
                            a[j][i] = 0
                        elif a[i][k] >= a[i][j] and a[i][k] >= a[j][k]:
                            a[i][k] = 0
                            a[k][i] = 0
                        else: 
                            a[j][k] = 0
                            a[k][j] = 0
  
def symmetry_test(a):
    if sum(np.matrix.trace(a)) != 0:
        return False
    return np.allclose(np.matrix.transpose(a), a)
            
def count_items(a):
    m = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] > 0:
                m += 1
    return m

def print_matrix(a):
    for i in range(len(a)):
        print
        for j in range(len(a)):
            print a[i][j],
  
if __name__ == '__main__':
    '''
    a = np.array([[0,16,12,21,0,0,0],
         [16,0,0,17,20,0,0],
         [12,0,0,28,0,31,0],
         [21,17,28,0,18,19,23],
         [0,20,0,18,0,0,11],
         [0,0,31,19,0,0,27],
         [0,0,0,23,11,27,0]])
         '''
    start = time.time()
    a = read_matrix() 
    #print a
    s = sum(a)/2
    print 'symmetry = ',symmetry_test(a)
    print s
    c = 1
    while c != 0:
        c = remove_max(a)
        print c
        print 'symmetry = ', symmetry_test(a)
        print sum(a)/2, s - sum(a)/2 
        print count_items(a)/2
    remove_tri(a)
    print count_items(a)/2
    print sum(a)/2, s - sum(a)/2
    print(time.time() - start)
        

