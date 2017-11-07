import time
start = time.time()

def make_grid(nx,ny):
    a = [i for i in range(nx)]
    b = [i for i in range(ny)]
    return (a,b)
    
def nbr_rect(x,y):
    s=0
    a,b = make_grid(x,y)    
    for n in b[0:-1]:
        for i in a[0:-1]:
            for j in b[n+1:]:
                for k in a[i+1:]:
                    s += 1
    return s
                        
pmax = []
pmin = []
for x in range(2,60):
    y = 45
    while nbr_rect(x,y) < 2000000:
        y += 1       
    pmax.append((x,y,nbr_rect(x,y)))
    pmin.append((x,y-1,nbr_rect(x,y-1)))

minpmax = pmax[0]   
for i in pmax[1:]:
    if minpmax[2] > i[2]:
        minpmax = i
print minpmax

maxpmin = pmin[0]   
for i in pmin[1:]:
    if maxpmin[2] < i[2]:
        maxpmin = i
print maxpmin
print time.time() - start        