names = open('names.txt')
b = names.readline()
    
for i in range(0,len(b)):
  a = b.split(',')
  
let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 

dict = {}
for i in range(1,27):
  dict[let[i-1:i]] = i
  
a.sort() 

count = 1  
total = 0  
for i in a:
  sum = 0
  for j in i:
    if j <> '\n': sum += dict[j]
  total += count*sum
  count += 1
  
print(total)

