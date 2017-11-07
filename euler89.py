
d = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

lines = open('roman.txt').read().splitlines()

save = 0
for i in lines:
    print i  
    len1 = len(i)
    tot = 0
    prev = 0
    for j in i:
        if prev < d[j]:
            tot -= 2*prev
        tot += d[j]
        prev = d[j]
    print tot
    
    n = ''
    if tot >= 4000:
        n += 'MMMM'
        tot -= 4000
    if tot >= 3900:
        n += 'CMMMM'
        tot -= 3900 
    if tot >= 3000:
        n += 'MMM'
        tot -= 3000
    if tot >= 2900:
        n += 'CMMM'
        tot -= 2900
    if tot >= 2000:
        n += 'MM'
        tot -= 2000
    if tot >= 1900:
        n += 'CMM'
        tot -= 1900 
    if tot >= 1000:
        n += 'M'
        tot -= 1000
    if tot >= 900:
        n += 'CM'
        tot -= 900 
    if tot >= 500:
        n += 'D'
        tot -= 500 
    if tot >= 400:
        n += 'CD'
        tot -= 400 
    if tot >= 300:
        n += 'CCC'
        tot -= 300
    if tot >= 200:
        n += 'CC'
        tot -= 200 
    if tot >= 100:
        n += 'C'
        tot -= 100 
    if tot >= 90:
        n += 'XC'
        tot -= 90
    if tot >= 50:
        n += 'L'
        tot -= 50 
    if tot >= 40:
        n += 'XL'
        tot -= 40
    if tot >= 30:
        n += 'XXX'
        tot -= 30
    if tot >= 20:
        n += 'XX'
        tot -= 20
    if tot >= 10:
        n += 'X'
        tot -= 10
    if tot >= 9:
        n += 'IX'
        tot -= 9
    if tot >= 8:
        n += 'VIII'
        tot -= 8
    if tot >= 7:
        n += 'VII'
        tot -= 7
    if tot >= 6:
        n += 'VI'
        tot -= 6
    if tot >= 5:
        n += 'V'
        tot -= 5
    if tot >= 4:
        n += 'IV'
        tot -= 4
    if tot >= 3:
        n += 'III'
        tot -= 3
    if tot >= 2:
        n += 'II'
        tot -= 2
    if tot >= 1:
        n += 'I'
        tot -= 1
    print n
    save += len1 - len(n)
print save