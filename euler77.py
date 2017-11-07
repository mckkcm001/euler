import time
import math
start = time.clock()

p=[2]
def isprime(n):
  for i in range(3,1 + int(math.pow(n,.5)),2):
    if n % i == 0:
      return False
  return True

for i in range(3,5,2):
    if isprime(i): 
        p.append(i)

def changes(amount, coins):
    ways = [0] * (amount + 1)
    #print ways
    ways[0] = 1
    for coin in coins:
       #print 'coin = '+ str(coin)
        for j in xrange(coin, amount + 1):
            #print j
            ways[j] += ways[j - coin]
            #print ways
    return ways[amount]
p= [i for i in range(1,4)]
print changes(4, p)

print(time.clock() - start)
