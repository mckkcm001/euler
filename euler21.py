divisors = [[]]

def findDivisors(n):
  a = []
  for i in range(1, n):
    if n%i == 0: a.append(i)
  return a
   
dict = {1:1}  
for i in range(2,30000):
  sum = 0
  for j in findDivisors(i):
    sum += j
  dict[i] = sum
 
sum = 0
for i in range(1,10000):
  if i == dict[dict[i]] and i <> dict[i]: 
    sum += i
    print(i,dict[i])

print(sum)
