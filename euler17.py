import math

hl = ['','onehundred','twohundred','threehundred','fourhundred','fivehundred','sixhundred','sevenhundred','eighthundred','ninehundred']
teenl = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tl = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
ol = ['','one','two','three','four','five','six','seven','eight','nine']

def word(n):
  s = ''
  h = int(n/100)
  t = int((n - h*100)/10)
  o = n - h*100 - t*10
  
  s = s + hl[h]
  if h != 0 and (t != 0 or o != 0):
    s = s + 'and'
  s = s + tl[t]
  if t == 1:
    s = s + teenl[o]
  if t != 1:
    s = s + ol[o]
  return s
  
def letters(n):
  sum = 0
  h = int(n/100)
  t = int((n - h*100)/10)
  o = n-h*100-t*10
  sum = sum + hl[h] + tl[t] + ol[o]
  if t == 0 and o == 0:
    sum = sum - 3
  if t == 1:
    sum = sum + teenl[t] - ol[o]
  return sum
  
sum = 0
for i in range(1,1000):
  sum = sum + len(word(i))
print(sum+11)
