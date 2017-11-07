from fractions import Fraction

rounds = 1
odds = Fraction(blue,blue+red)

def chances(rounds):
  red = 0
  blue = 0
  bag_red = 1
  bag_blue = 1
  for i in range(rounds):
    
  
for i in range(rounds):
  red += 1
  odds *= Fraction(blue,blue+red)

print(odds)
