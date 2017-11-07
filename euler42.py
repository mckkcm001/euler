import time
from itertools import permutations
start = time.clock()
tri = []

for i in range(1,50):
    tri.append(i*(i+1)/2)

a = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,
'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

f = open('words.txt')
line = f.readline()
words = line.split('","')
words[0] = 'A'
words[len(words)-1] = 'YOUTH'

n = 0
for i in words:
  sum = 0
  for j in i:
    sum += a[j]
  if sum in tri:
    n += 1

print(n)

print(time.clock() - start)
