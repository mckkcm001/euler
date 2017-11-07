import time
import random
import operator

start = time.clock()

b = [i for i in range(40)]
p = [0]*40
p = dict(zip(b, p))

cc = [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ch = [1,2,3,4,5,6,7,8,9,10,0,0,0,0,0,0]
random.shuffle(cc)
random.shuffle(ch)
ccc = -1
chc = -1

def roll():
    d1 = random.randint(1,4)
    d2 = random.randint(1,4)
    return (d1,d2)

def comm():
    global pl,ccc
    ccc = (ccc + 1)%16
    if cc[ccc] == 1: 
        pl = 0
        p[0] += 1
    elif cc[ccc] == 2:
        pl = 10
        p[10] += 1
    else:
        p[pl] += 1
        
def chan():
    global pl,chc,ccc
    chc = (chc + 1)%16
    if ch[chc] == 1: 
        pl = 0
        p[0] += 1
    elif ch[chc] == 2:
        pl = 10
        p[10] += 1
    elif ch[chc] == 3: 
        pl = 11
        p[11] += 1
    elif ch[chc] == 4:
        pl = 24
        p[24] += 1
    elif ch[chc] == 5: 
        pl = 39
        p[39] += 1
    elif ch[chc] == 6:
        pl = 5
        p[5] += 1
    elif ch[chc] == 7 or ch[chc] == 8: 
        if pl == 36:
            pl = 5
            p[5] += 1
        elif pl == 7:
            pl = 15
            p[15] += 1
        elif pl == 22:
            pl = 25
            p[25] += 1
    elif ch[chc] == 9: 
        if pl == 36:
            pl = 12
            p[12] += 1
        elif pl == 7:
            pl = 12
            p[12] += 1
        elif pl == 22:
            pl = 28
            p[28] += 1
    elif ch[chc] == 10:
        pl -= 3
        if pl == 33:
            comm()
        else:
            p[pl] += 1
    else:
        p[pl] += 1
        
pl = 0
trip = 0       
for i in range(10000000):
    r = roll()
    if r[0] == r[1]:
        trip += 1
        if trip == 3 :
            pl = 10
            trip = 0
        else:
            pl = (pl + r[0]+r[1])%40
    else:
        trip = 0
        pl = (pl + r[0]+r[1])%40
  
    if pl == 0: 
        p[0] += 1
    elif pl == 1: 
        p[1] += 1
    elif pl == 2: 
        comm()
    elif pl == 3: 
        p[3] += 1
    elif pl == 4: 
        p[4] += 1
    elif pl == 5: 
        p[5] += 1
    elif pl == 6: 
        p[6] += 1
    elif pl == 7: 
        chan()
    elif pl == 8: 
        p[8] += 1
    elif pl == 9: 
        p[9] += 1
    elif pl == 10: 
        p[10] += 1
    elif pl == 11: 
        p[11] += 1
    elif pl == 12: 
        p[12] += 1
    elif pl == 13: 
        p[13] += 1
    elif pl == 14: 
        p[14] += 1
    elif pl == 15: 
        p[15] += 1
    elif pl == 16: 
        p[16] += 1
    elif pl == 17: 
        comm()
    elif pl == 18: 
        p[18] += 1
    elif pl == 19: 
        p[19] += 1
    elif pl == 20: 
        p[20] += 1
    elif pl == 21: 
        p[21] += 1
    elif pl == 22: 
        chan()
    elif pl == 23: 
        p[23] += 1
    elif pl == 24: 
        p[24] += 1
    elif pl == 25: 
        p[25] += 1
    elif pl == 26: 
        p[26] += 1
    elif pl == 27: 
        p[27] += 1
    elif pl == 28: 
        p[28] += 1
    elif pl == 29: 
        p[29] += 1
    elif pl == 30: 
        pl = 10
        p[10] += 1
    elif pl == 31: 
        p[31] += 1
    elif pl == 32: 
        p[32] += 1
    elif pl == 33: 
        comm()
    elif pl == 34: 
        p[34] += 1
    elif pl == 35: 
        p[35] += 1
    elif pl == 36: 
        chan()
    elif pl == 37: 
        p[37] += 1
    elif pl == 38: 
        p[38] += 1
    elif pl == 39: 
        p[39] += 1
 
tot = sum(p.values()) 
print tot

sorted_p = reversed(sorted(p.iteritems(), key=operator.itemgetter(1)))
for i in sorted_p:
    print i[0], 100.*i[1]/tot
    
print(time.clock() - start)
