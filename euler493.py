import time
from fractions import Fraction
import itertools
start = time.time()

def c(n,k):
    t=1
    for i in range(k):
        t *= Fraction(n-i,k-i)
    return t
d2 = [[10,10]]  
d3=[]  
for a1 in range (10,0,-1):
    #print a1
    for a2 in range(a1,0,-1):
        for a3 in range(a2,0,-1):
            if a1 + a2 + a3 == 20:
                d3.append([a1,a2,a3])
d4=[]  
for a1 in range (10,0,-1):
    #print a1
    for a2 in range(a1,0,-1):
        for a3 in range(a2,0,-1):
            for a4 in range(a3,0,-1):
                if a1 + a2 + a3 + a4 == 20:
                    d4.append([a1,a2,a3,a4])

d5=[]  
for a1 in range (10,0,-1):
    #print a1
    for a2 in range(a1,0,-1):
        for a3 in range(a2,0,-1):
            for a4 in range(a3,0,-1):
                for a5 in range(a4,0,-1):
                    if a1 + a2 + a3 + a4 + a5 == 20:
                        d5.append([a1,a2,a3,a4,a5])
                        
d6=[]  
for a1 in range (10,0,-1):
    #print a1
    for a2 in range(a1,0,-1):
        for a3 in range(a2,0,-1):
            for a4 in range(a3,0,-1):
                for a5 in range(a4,0,-1):
                    for a6 in range(a5,0,-1):
                       if a1 + a2 + a3 + a4 + a5 + a6 == 20:
                           d6.append([a1,a2,a3,a4,a5,a6])                        
                        
d7=[]  
for a1 in range (10,0,-1):
    #print a1
    for a2 in range(a1,0,-1):
        for a3 in range(a2,0,-1):
            for a4 in range(a3,0,-1):
                for a5 in range(a4,0,-1):
                    for a6 in range(a5,0,-1):
                        for a7 in range(a6,0,-1):
                            if a1 + a2 + a3 + a4 + a5 + a6 + a7 == 20:
                                d7.append([a1,a2,a3,a4,a5,a6,a7])                                                
                        
#print d2
#print d3
#print d4    
#print d5 
#print d6  
#print d7
t = c(70,20)
s2 = 0
for i in d2:
    p2 = 1
    for j in i:
        p2 *= c(10,j) 
    p2 = Fraction(p2,t)
    n=7
    for j in list(set(i)):
        p2 *= c(n,i.count(j))
        n -= i.count(j)
    s2+=p2
print float(s2)
    
s3 = 0
for i in d3:
    p3 = 1
    for j in i:
        p3 *= c(10,j) 
    p3 = Fraction(p3,t)
    n=7
    for j in list(set(i)):
        p3 *= c(n,i.count(j))
        n -= i.count(j)
    s3+=p3
print float(s3)
 
s4 = 0
for i in d4:
    p4 = 1
    for j in i:
        p4 *= c(10,j) 
    p4 = Fraction(p4,t)
    n=7
    for j in list(set(i)):
        p4 *= c(n,i.count(j))
        n -= i.count(j)
    s4+=p4
print float(s4)
    
s5 = 0
for i in d5:
    p5 = 1
    for j in i:
        p5 *= c(10,j) 
    p5 = Fraction(p5,t)
    n=7
    for j in list(set(i)):
        p5 *= c(n,i.count(j))
        n -= i.count(j)
    s5+=p5
print float(s5)  

s6 = 0
for i in d6:
    p6 = 1
    for j in i:
        p6 *= c(10,j) 
    p6 = Fraction(p6,t)
    n=7
    for j in list(set(i)):
        p6 *= c(n,i.count(j))
        n -= i.count(j)
    s6+=p6
print float(s6)
    
s7 = 0
for i in d7:
    p7 = 1
    for j in i:
        p7 *= c(10,j) 
    p7 = Fraction(p7,t)
    n=7
    for j in list(set(i)):
        p7 *= c(n,i.count(j))
        n -= i.count(j)
    s7+=p7
print float(s7)

print float(s2 + s3 + s4 + s5 +s6 + s7)

print float(2*s2 + 3*s3 + 4*s4 + 5*s5 +6*s6 + 7*s7)
    
print time.time() - start