import time
start = time.clock()


from fractions import Fraction

a=set()
for d in range(2,10000):
    for n in range(1,d):
        a.add(Fraction(n,d))

print(len(a))

print(time.clock() - start)
