import time
import operator

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
    return a
    
def print_matrix(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print a[i][j],
        print
        
def vertex_matrix(a):
    d = {}
    for i in range(len(a)):
        d[i] = []
        for j in range(len(a)):
            if a[i][j] > 0:
                d[i].append(j)
    return d

def sorted_dict_matrix(a):
    d={}
    for i in range(len(a)):
        for j in range(len(a)):
            d[(i,j)] = a[i][j]  
    return sorted(d.items(), key=operator.itemgetter(1), reverse = True)
    
def connected(d,vd=None,vs=None):
    if vd is None:
        vd = set()
    v = d.keys()
    if not vs:
        vs = v[0]
    vd.add(vs)
    if len(vd) != len(v):
        for k in d[vs]:
            if k not in vd:
                if connected(d,vd,k):
                    return True
    else:
        return True
    return False

def max_matrix(a):
    m = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] > m:
                m = a[i][j]
                x,y = i,j
    return m,x,y

                         
if __name__ == '__main__':
    start = time.time()
    '''
    a = [[0,16,12,21,0,0,0],
         [16,0,0,17,20,0,0],
         [12,0,0,28,0,31,0],
         [21,17,28,0,18,19,23],
         [0,20,0,18,0,0,11],
         [0,0,31,19,0,0,27],
         [0,0,0,23,11,27,0]]
         '''
    a = read_matrix()
    
    d = sorted_dict_matrix(a)
    s = sum(a)/2
    for k in d:
        print k[1]
        a[k[0][0]][k[0][1]] = 0
        a[k[0][1]][k[0][0]] = 0
        v = vertex_matrix(a)
        if not connected(v):
            a[k[0][0]][k[0][1]] = k[1]
            a[k[0][1]][k[0][0]] = k[1]
        
    print s-sum(a)/2
    print(time.time() - start)

