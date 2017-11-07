def factorial(n):
  if n == 1: return 1
  else: return n*factorial(n-1)
  
sum = 0
for i in str(factorial(100)):
  sum += int(i)
  
print(sum)
