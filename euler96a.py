import time
from itertools import product
start = time.clock()

a = 'ABCDEFGHI'
d = '123456789'

s = [j+i for i in d for j in a]
c = [[j+i for i in d] for j in a]
r = [[j+i for j in a] for i in d]
u = [[j+i for i in n for j in m] for n in ['123','456','789'] for m in ['ABC','DEF','GHI']]
p = dict((i,[j for j in r[int(i[1:2])-1] if j != i]+\
            [j for j in c[ord(i[0:1])-65] if j != i]+\
            [j for j in u[(((int(i[1:2])-1)//3*3)+((ord(i[0:1])-65)//3))] if j != i]) for i in s )

with open('euler50.txt') as h:
    grids = h.read().splitlines()
    
def get_grid(n):
    gn = {i: d for i in s}
    for i,j in enumerate(grids[n]):
        if j in d:
            gn[a[i%9:i%9+1]+str(i//9+1)] = j
    return gn

def display(g):
    w = max([len(g[x]) for x in g])+2
    for j,i in enumerate(r):
        print('{0:^{w}}{1:^{w}}{2:^{w}}|{3:^{w}}{4:^{w}}{5:^{w}}|{6:^{w}}{7:^{w}}{8:^{w}}'.\
              format(g[i[0]],g[i[1]],g[i[2]],g[i[3]],g[i[4]],g[i[5]],g[i[6]],g[i[7]],g[i[8]],w=w))
        if j == 2 or j == 5:
            print('{0:^{w}}{0:^{w}}{0:^{w}}{1}{0:^{w}}{0:^{w}}{0:^{w}}{1}{0:^{w}}{0:^{w}}{0:^{w}}'.\
                  format('-'*w,'+',w=w))
    print()

def elim(i,ge):
    done = True
    for j in p[i]:
        if i == j: continue
        if ge[i] in ge[j]:
            ge[j]=ge[j].replace(ge[i],'')
            done = (False,ge)
    return (done,ge)

def onlyrow(r,i,gr):
    for n in gr[i]:
        only = True
        for j in r:
            if i == j: continue
            if n in gr[j]:
                only = False
        if only:
            gr[i]= n
            return (False,gr)
    return (True,gr)

def onlycol(c,i,gc):
    for n in gc[i]:
        only = True
        for j in c:
            if i == j: continue
            if n in gc[j]:
                only = False
        if only:
            gc[i]= n
            return (False,gc)
    return (True,gc)

def onlyunit(u,i,gu):
    for n in gu[i]:
        only = True
        for j in u:
            if i == j: continue
            if n in gu[j]:
                only = False
        if only :
            gu[i]= n
            return (False,gu)
    return (True,gu)
        
def solve(gs):
    d1 = True
    d2 = True
    for i in s:            
        if len(gs[i]) > 1:
            d1 = onlyrow(r[int(i[1:2])-1],i,gs) and \
                 onlycol(c[ord(i[0:1])-65],i,gs) and \
                 onlyunit(u[(((int(i[1:2])-1)//3*3)+((ord(i[0:1])-65)//3))],i,gs)
            
    d2 = all([elim(i,gs) for i in s if len(gs[i]) == 1])
    return (d1 and d2,gs)

def solved(gsol):
  if all(len(gsol[i]) == 1 for i in s):
    return True
  return False

def guess(gg):
  m = min([len(gg[i]) for i in s if len(gg[i]) > 1 ])
  display(gg)
  for i in gg:
    print(i,gg[i])
    if len(gg[i]) == m:
        g1 = gg
        for j in gg[i]:
          g1[i] = j
          display(g1)
          print(j)
          while not solve(g1):
            pass
          if any([len(g1[i]) for i in s if len(g1[i]) < 1 ]):
            continue
          if solved(g1):
            display(g1)
          else:
            guess(g1)
          
for i in range(5,6):
    g = get_grid(i)
    print('puzzle = '+str(i))
    display(g)
    done = False
    while not solve(g):
        pass
        #display(g)
    display(g)
    if solved(g):
        display(g)
    else:
        guess(g)   
            
print(time.clock() - start)
