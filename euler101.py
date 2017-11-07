import time
import numpy
import math

start = time.time()

def poly10(n):
    return 1 - n + math.pow(n,2) - math.pow(n,3) \
           + math.pow(n,4) - math.pow(n,5) + math.pow(n,6)\
           - math.pow(n,7) + math.pow(n,8) - math.pow(n,9) + math.pow(n,10)

def poly3(n):
    return  math.pow(n,3)

U10 =[]
U3 =[] 
for n in range(1, 12):
    U10.append(poly10(n))
    U3.append(poly3(n))

def get_poly10(n):
    x = numpy.array(range(1, n+1))
    y = numpy.array([poly10(k) for k in x])
    z = numpy.polyfit(x, y, n-1)
    return [round(i) for i in z]  

def get_poly3(n):
    x = numpy.array(range(1, n+1))
    y = numpy.array([poly3(k) for k in x])
    z = numpy.polyfit(x, y, n-1)
    return [round(i) for i in z]

def eval_poly(c):
    term = 0
    for j in range(0,len(c)):
        term += c[j]*math.pow(n,len(c)-j-1)
    return term
        
FIT = {}

for i in range(1,12):
  c = get_poly10(i)
  U=[]
  for n in range(1,12):
      #print "n = " + str(n) + ": "+str(eval_poly(c))
      U.append(eval_poly(c))
  print U
  print U10
  for j in range(0,len(U)):
      print U[j],U10[j]
      if U[j] != U10[j]:
        FIT[i] = U[j]
        break
   

print FIT, sum(FIT.values())
print(time.time() - start)        

