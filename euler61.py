import time
from itertools import permutations, combinations,product
start = time.clock()

tr = []
sq = []
pn = []
hx = []
hp = []
oc = []
for i in range(1,220):
  if len(str(i*(i+1)//2)) == 4:
    tr.append(i*(i+1)//2)
  if len(str(i*i)) == 4:
    sq.append(i*i)
  if len(str(i*(3*i-1)//2)) == 4:
    pn.append(i*(3*i-1)//2)
  if len(str(i*(2*i-1))) == 4:
    hx.append(i*(2*i-1))
  if len(str(i*(5*i-3)//2)) == 4:
    hp.append(i*(5*i-3)//2)
  if len(str(i*(3*i-2))) == 4:
    oc.append(i*(3*i-2))

c = [sq,pn,hx,hp,oc]
for t in tr:
  #print(t)
  for s in permutations(c):
    for i0 in s[0]:
      #print (i0)
      if str(t)[2:] == str(i0)[0:2]:
        for i1 in s[1]:
          #print(t,i0,i1)
          if str(i0)[2:] == str(i1)[0:2]:
            for i2 in s[2]:
              #print(t,i0,i1,i2)
              if str(i1)[2:] == str(i2)[0:2]:
                for i3 in s[3]:
                  #print(t,i0,i1,i2,i3)
                  if str(i2)[2:] == str(i3)[0:2]:
                    for i4 in s[4]:
                      #print(t,i0,i1,i2,i3,i4)
                      if str(i3)[2:] == str(i4)[0:2]:
                        if str(i4)[2:] == str(t)[0:2]:
                          print(t,i0,i1,i2,i3,i4)



print(time.clock() - start)
