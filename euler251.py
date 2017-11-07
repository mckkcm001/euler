import math

def Q(a1,a2):
    return (3.*a1 - a2**2.)/9.
    
def R(a0,a1,a2):
    return (9.*a1*a2 - 27.*a0 - 2.*math.pow(a2,3.))/54.

def D(R,Q):
    return math.pow(Q,3.) + math.pow(R,2.)
    
def S(R,D):
    return math.pow(R + math.pow(D,0.5),1./3.)
    
def T(R,D):
    if R - math.pow(D,0.5) > 0:
      return math.pow(R - math.pow(D,0.5),1./3.)
    else:
      return -math.pow(-R + math.pow(D,0.5),1./3.)
      
for a2 in range(1,5):
   for a1 in range(1,5):
       for a0 in range(1,5):
           q = Q(a1,a2)
           r = R(a0,a1,a2)
           d = D(r,q)
           s = S(r,d)
           t = T(r,d)
           print a2,a1,a0
           print q,r,d,s,t
           print s + t