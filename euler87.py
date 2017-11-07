import time
start = time.clock()

def isprime(n):
  for i in range(3,1 + int(math.pow(n,.5)),2):
    if n % i == 0:
      return False
  return True
p = [2]
for i in range(3,7100,2): 
    if isprime(i):
        p.append(i)
s = set()
for i in p:
    if i**2 > 50000000:
        print i, i**2
        break
    for j in p:
        if j**3 > 50000000:
            print j, j**3
            break
        for k in p:
            if k**4 > 50000000:
                print k, k**4
                break
            if i**2 + j**3 + k**4 < 50000000:
                s.add(i**2+j**3+k**4)
                
print len(s)               
print(time.clock() - start)                
              