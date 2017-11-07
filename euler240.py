import time
start = time.clock()

s=[]
n=12

#cents = 70
#denominations = [12,11,10,9,8,7,6,5,4,3,2,1]
#names = {12:12,11:11,10:10,9:9,8:8,7:7,6:6,5:5,4:4,3:3,2:2,1:1}

cents = 15
denominations = [6,5,4,3,2,1]
names = {6:6,5:5,4:4,3:3,2:2,1:1}

b = []

def count_combs(left, i, comb, add):
    if add: comb.append(add)
    if left == 0 or (i+1) == len(denominations):
        if (i+1) == len(denominations) and left > 0:
            comb.append( (left, denominations[i]) )
            i += 1
        while i < len(denominations):
            comb.append( (0, denominations[i]) )
            i += 1
        s = 0
        a = []
        for i in comb:
            s += i[0]
            for j in range(i[0]):
                a.append(i[1])
        if s == 3:
            b.append(a)
        return 1
    cur = denominations[i]
    return sum(count_combs(left-x*cur, i+1, comb[:], (x,cur)) for x in range(0, int(left/cur)+1))

print count_combs(cents, 0, [], None)

s=0
for i in b:
    
    for j in range(1,b[2]+1):
        for k in range(1,b[2]+1):
            


print time.clock()-start