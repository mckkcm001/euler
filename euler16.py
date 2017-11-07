import math
a = str(int(math.pow(2,1000)))
sum = 0
for i in range(0,len(a)):
  sum = sum + int(a[i:i+1])
print(sum)
