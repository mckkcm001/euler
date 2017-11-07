import itertools
b = []
s = '0123456789'
a = itertools.permutations(s,10)
#a.sort()
for i in a:
  s = ''
  for j in i:
    s += j
  b.append(s)
b.sort()
print(b[999999])
