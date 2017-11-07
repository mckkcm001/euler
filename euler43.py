import time
from itertools import permutations
start = time.clock()

n = [0,1,2,3,4,5,6,7,8,9]

sum = 0
for i in permutations(n):
  if (i[1]*100+i[2]*10+i[3])%2 == 0 \
  and (i[2]*100+i[3]*10+i[4])%3 == 0 \
  and (i[3]*100+i[4]*10+i[5])%5 == 0 \
  and (i[4]*100+i[5]*10+i[6])%7 == 0 \
  and (i[5]*100+i[6]*10+i[7])%11 == 0 \
  and (i[6]*100+i[7]*10+i[8])%13 == 0 \
  and (i[7]*100+i[8]*10+i[9])%17 == 0:
    s = ''
    for j in i:
      s += str(j)
    sum += int(s)

print(sum)

print(time.clock() - start)
