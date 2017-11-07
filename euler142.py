import time
start = time.time()

def factors(val):
    return [(i, val / i) for i in range(1, int(val**0.5)+1) 
                    if val % i == 0]
       
def get_triples(n):
    if n%2 == 0:
        return [[2*i[0]*i[1],i[1]**2-i[0]**2,i[1]**2+i[0]**2] 
            for i in factors(n/2)]
    else:
        return [[i[0]*i[1],(i[1]**2-i[0]**2)/2,(i[1]**2+i[0]**2)/2] 
            for i in factors(n)]   

tp = {}
mmin = 300
mmax = 303
nmax = 400
for m in range(mmin,mmax):
    for n in range(m+1,nmax):
        xx = (n*n - m*m)**2
        yy = 4*n*n*m*m
        rr = (n*n+m*m)**2
        f = min(xx,yy)
        e = max(xx,yy)
        d = rr
        ecb = [[e,i[1]**2,i[2]**2] for i in get_triples(e**.5) if i[2] > d**.5]
        if ecb != []:
            for j in ecb:
                fba = [[f,j[2],i[2]**2] for i in get_triples(f**.5) if i[1]**2 == j[2]]
                cda = [[j[1],i[1]**2,i[2]**2] for i in get_triples(j[1]**.5)]
        for i in fba:
            for j in cda:
                if i[2] == j[2]:
                    print (j[0] + j[2] + i[1])/2
print time.time() - start