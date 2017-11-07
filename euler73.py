import time
start = time.clock()

from fractions import Fraction

a=set()
for d in range(2,12001):
    for n in range(d//3+1,d//2+1):
        if Fraction(n,d) > Fraction(1,3) and Fraction(n,d) < Fraction(1,2):
            a.add(Fraction(n,d))

print(len(a))
print(time.clock() - start)
