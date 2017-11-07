import time
from itertools import permutations, combinations,product
start = time.clock()

c ={}
for i in range(1,10000):
  c[i*i*i]=''.join(sorted(str(i*i*i)))

new_dict = {}
for k, v in c.items():
    new_dict.setdefault(v, []).append(k)

for i in new_dict.keys():
  if len(new_dict[i]) == 5:
    print(new_dict[i])

print(time.clock() - start)
