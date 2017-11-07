import math

def factors(n):
  a = []
  for i in range(1,1+int(math.pow(n,.5))):
    if n % i == 0:
      a.append(i)
      a.append(int(n/i))
  return a 
     
def triangle(n):
  sum = 1
  for i in range(2,n+1):
    sum+=i
  return sum

n = 3
done = False
while done == False:
  if len(factors(triangle(n))) > 500:
    print(triangle(n))
    done = True
  else:
    n+=1
    
    
