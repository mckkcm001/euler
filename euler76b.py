import time
start = time.clock()

def choose(n,r):
  """Computes n! / (r! (n-r)!) exactly. Returns a python long int."""
  assert n >= 0
  assert 0 <= r <= n

  c = 1
  denom = 1
  for (num,denom) in zip(range(n,n-r,-1), range(1,r+1,1)):
    c = (c * num) // denom
  return c
                        
print(choose(7,5))

print(time.clock() - start)
