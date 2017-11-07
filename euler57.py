import time
from fractions import Fraction
start = time.clock()

s = 0
f = fractions.Fraction(1,2)
for i in range(1000):
  #print(f)
  if len(str(f.numerator + f.denominator)) > len(str(f.denominator)):
    s += 1
  f = fractions.Fraction(1,2+f)

print(s)

print(time.clock() - start)
