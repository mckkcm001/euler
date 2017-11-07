import time
from itertools import permutations, combinations
start = time.clock()

words = open('words98.txt')
line = words.read()
a=line.replace('"','').split(',')
words.close()

def isAnagram(s1,s2):
  return sorted(list(s1)) == sorted(list(s2))

p=[[],[],[],[],[],[],[],[],[],[]]
for pair in combinations(a,2):
  if isAnagram(pair[0],pair[1]):
    p[len(pair[0])].append(pair)

print(p)

r=[]
m = 0
for i in p:
  for j in i:
    for perm in permutations('0123456789',len(j[0])):
      if perm[0] == '0': continue
      n1 = int("".join(perm))
      if pow(int(pow(n1,0.5)),2) == n1:
        d = dict(zip(j[0],perm))
        if d[j[1][0]] == '0': continue
        n2 = int(''.join([d[l] for l in j[1]]))
        if pow(int(pow(n2,0.5)),2) == n2:
          r.append((n1,str(n2)))
          if n1 > m: m = n1
          if n2 > m: m = n2
print(r)
print(m)

print(time.clock() - start)
