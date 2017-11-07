import fractions
n = []
d = []

for i in range(11,98):
    if i%10 == 0:
        continue
    for j in range(i+1,99):
        if j%10 == 0:
            continue       
        if i//10 == j//10 and fractions.Fraction(i,j) == fractions.Fraction((i%10),(j%10)):
            n.append(i)
            d.append(j)
        if i//10 == j%10 and fractions.Fraction(i,j) == fractions.Fraction((i%10),(j//10)):
            n.append(i)
            d.append(j)
        if i%10 == j//10 and fractions.Fraction(i,j) == fractions.Fraction((i//10),(j%10)):
            n.append(i)
            d.append(j)    
        if i%10 == j%10 and fractions.Fraction(i,j) == fractions.Fraction((i//10),(j//10)):
            n.append(i)
            d.append(j)                            
                        
print(fractions.Fraction(n[0],d[0])*fractions.Fraction(n[1],d[1])*fractions.Fraction(n[2],d[2])*fractions.Fraction(n[3],d[3]))
