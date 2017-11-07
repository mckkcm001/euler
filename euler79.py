import time
from itertools import permutations
start = time.clock()

keylog = []
logs = open('keylog.txt')
for line in logs:
    keylog.append(line.strip())

for i in permutations(['1','2','3','0','7','8','9','6']):
    test = True
    for j in keylog:
        s = list(i)
        if s.index(j[0:1]) > s.index(j[1:2])  \
        or s.index(j[0:1]) > s.index(j[2:3])  \
        or s.index(j[1:2]) > s.index(j[2:3]):
            test = False
            break
    if test:
        print i
            

print(time.clock() - start)
