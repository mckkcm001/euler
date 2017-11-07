import time
from itertools import permutations, combinations
start = time.clock()

def flush(h):
    if h[0][1] == h[1][1] == h[2][1] == h[3][1] == h[4][1]:
        return True
    return False

def straight(h):
    o = set([h[0][0:1],h[1][0:1],h[2][0:1],h[3][0:1],h[4][0:1]])
    s = [set(['2','3','4','5','A']),
         set(['2','3','4','5','6']),
         set(['3','4','5','6','7']),
         set(['4','5','6','7','8']),
         set(['5','6','7','8','9']),
         set(['6','7','8','9','T']),
         set(['7','8','9','T','J']),
         set(['8','9','T','J','Q']),
         set(['9','T','J','Q','K']),
         set(['T','J','Q','K','A'])]
    if o in s:
        return True
    return False

def val(n):
    if n[0:1] == '2': return 0
    if n[0:1] == '3': return 1
    if n[0:1] == '4': return 2
    if n[0:1] == '5': return 3
    if n[0:1] == '6': return 4
    if n[0:1] == '7': return 5
    if n[0:1] == '8': return 6
    if n[0:1] == '9': return 7
    if n[0:1] == 'T': return 8
    if n[0:1] == 'J': return 9
    if n[0:1] == 'Q': return 10
    if n[0:1] == 'K': return 11
    if n[0:1] == 'A': return 12
    
def four(h):
    if h[0][0] == h[1][0] == h[2][0] == h[3][0]: return (True,h[0][0])
    if h[0][0] == h[1][0] == h[2][0] == h[4][0]: return (True,h[0][0])
    if h[0][0] == h[1][0] == h[3][0] == h[4][0]: return (True,h[0][0])
    if h[0][0] == h[2][0] == h[3][0] == h[4][0]: return (True,h[0][0])
    if h[1][0] == h[2][0] == h[3][0] == h[4][0]: return (True,h[1][0])
    return (False,)

def pair2(h):
    if h[0][0] == h[1][0]:
        if h[2][0] == h[3][0]: return (True, h[0][0], h[2][0], h[4][0])
        if h[2][0] == h[4][0]: return (True, h[0][0], h[2][0], h[3][0])
        if h[3][0] == h[4][0]: return (True, h[0][0], h[3][0], h[2][0])
    if h[0][0] == h[2][0]:
        if h[1][0] == h[3][0]: return (True, h[0][0], h[1][0], h[4][0])
        if h[1][0] == h[4][0]: return (True, h[0][0], h[1][0], h[3][0])
        if h[3][0] == h[4][0]: return (True, h[0][0], h[3][0], h[1][0])
    if h[0][0] == h[3][0]:
        if h[1][0] == h[2][0]: return (True, h[0][0], h[1][0], h[4][0])
        if h[1][0] == h[4][0]: return (True, h[0][0], h[1][0], h[2][0])
        if h[2][0] == h[4][0]: return (True, h[0][0], h[2][0], h[1][0])
    if h[0][0] == h[4][0]:
        if h[1][0] == h[2][0]: return (True, h[0][0], h[1][0], h[3][0])
        if h[1][0] == h[3][0]: return (True, h[0][0], h[1][0], h[2][0])
        if h[2][0] == h[3][0]: return (True, h[0][0], h[2][0], h[1][0])
    if h[1][0] == h[2][0]:
        if h[0][0] == h[3][0]: return (True, h[1][0], h[0][0], h[4][0])
        if h[0][0] == h[4][0]: return (True, h[1][0], h[0][0], h[3][0])
        if h[3][0] == h[4][0]: return (True, h[1][0], h[3][0], h[0][0])
    if h[1][0] == h[3][0]:
        if h[0][0] == h[2][0]: return (True, h[1][0], h[0][0], h[4][0])
        if h[0][0] == h[4][0]: return (True, h[1][0], h[0][0], h[2][0])
        if h[2][0] == h[4][0]: return (True, h[1][0], h[2][0], h[0][0])
    if h[1][0] == h[4][0]:
        if h[0][0] == h[2][0]: return (True, h[1][0], h[0][0], h[3][0])
        if h[0][0] == h[3][0]: return (True, h[1][0], h[0][0], h[2][0])
        if h[2][0] == h[3][0]: return (True, h[1][0], h[2][0], h[0][0])
    if h[2][0] == h[3][0]:
        if h[0][0] == h[1][0]: return (True, h[2][0], h[0][0], h[4][0])
        if h[0][0] == h[4][0]: return (True, h[2][0], h[0][0], h[1][0])
        if h[1][0] == h[4][0]: return (True, h[2][0], h[1][0], h[0][0])
    if h[2][0] == h[4][0]:
        if h[0][0] == h[1][0]: return (True, h[2][0], h[0][0], h[3][0])
        if h[0][0] == h[3][0]: return (True, h[2][0], h[0][0], h[1][0])
        if h[1][0] == h[3][0]: return (True, h[2][0], h[1][0], h[0][0])
    if h[3][0] == h[4][0]:
        if h[0][0] == h[1][0]: return (True, h[3][0], h[0][0], h[2][0])
        if h[0][0] == h[2][0]: return (True, h[3][0], h[0][0], h[1][0])
        if h[1][0] == h[2][0]: return (True, h[3][0], h[1][0], h[0][0])
    return (False,)

def full(h):
    if h[0][0] == h[1][0] == h[2][0] and h[3][0] == h[4][0]: return (True,h[0][0])
    if h[0][0] == h[1][0] == h[3][0] and h[2][0] == h[4][0]: return (True,h[0][0])
    if h[0][0] == h[1][0] == h[4][0] and h[3][0] == h[2][0]: return (True,h[0][0])
    if h[0][0] == h[2][0] == h[3][0] and h[1][0] == h[4][0]: return (True,h[0][0])
    if h[0][0] == h[2][0] == h[4][0] and h[3][0] == h[1][0]: return (True,h[0][0])
    if h[0][0] == h[3][0] == h[4][0] and h[1][0] == h[2][0]: return (True,h[0][0])
    if h[1][0] == h[2][0] == h[3][0] and h[0][0] == h[4][0]: return (True,h[1][0])
    if h[1][0] == h[2][0] == h[4][0] and h[3][0] == h[0][0]: return (True,h[1][0])
    if h[1][0] == h[3][0] == h[4][0] and h[0][0] == h[2][0]: return (True,h[1][0])
    if h[2][0] == h[3][0] == h[4][0] and h[0][0] == h[1][0]: return (True,h[2][0])
    return (False,)

def trip(h):
    if h[0][0] == h[1][0] == h[2][0]: return (True,h[0][0])
    if h[0][0] == h[1][0] == h[3][0]: return (True,h[0][0])
    if h[0][0] == h[1][0] == h[4][0]: return (True,h[0][0])
    if h[0][0] == h[2][0] == h[3][0]: return (True,h[0][0])
    if h[0][0] == h[2][0] == h[4][0]: return (True,h[0][0])
    if h[0][0] == h[3][0] == h[4][0]: return (True,h[0][0])
    if h[1][0] == h[2][0] == h[3][0]: return (True,h[1][0])
    if h[1][0] == h[2][0] == h[4][0]: return (True,h[1][0])
    if h[1][0] == h[3][0] == h[4][0]: return (True,h[1][0])
    if h[2][0] == h[3][0] == h[4][0]: return (True,h[2][0])
    return (False,)

def pair(h):
    if h[0][0] == h[1][0]: return (True, h[0][0],h[2][0],h[3][0],h[4][0])
    if h[0][0] == h[2][0]: return (True, h[0][0],h[1][0],h[3][0],h[4][0])
    if h[0][0] == h[3][0]: return (True, h[0][0],h[1][0],h[2][0],h[4][0])
    if h[0][0] == h[4][0]: return (True, h[0][0],h[2][0],h[3][0],h[1][0])
    if h[1][0] == h[2][0]: return (True, h[1][0],h[0][0],h[3][0],h[4][0])
    if h[1][0] == h[3][0]: return (True, h[1][0],h[2][0],h[0][0],h[4][0])
    if h[1][0] == h[4][0]: return (True, h[1][0],h[2][0],h[3][0],h[0][0])
    if h[2][0] == h[3][0]: return (True, h[2][0],h[0][0],h[1][0],h[4][0])
    if h[2][0] == h[4][0]: return (True, h[2][0],h[0][0],h[3][0],h[1][0])
    if h[3][0] == h[4][0]: return (True, h[3][0],h[2][0],h[1][0],h[0][0])
    return (False,)

def eval(h):
    if straight(h) and flush(h):
       if h[0][0] == '2' and h[4][0] == '6': return 9*13+1
       if h[0][0] == '2' and h[4][0] == 'A': return 9*13+0
       if h[0][0] == '3': return 9*13+2
       if h[0][0] == '4': return 9*13+3
       if h[0][0] == '5': return 9*13+4
       if h[0][0] == '6': return 9*13+5
       if h[0][0] == '7': return 9*13+6
       if h[0][0] == '8': return 9*13+7
       if h[0][0] == '9': return 9*13+8
       if h[0][0] == 'A': return 9*13+9
    if four(h)[0]:
       return 8*13 + val(four(h)[1])
    if full(h)[0]:
        return 7*13 + val(trip(h)[1])
    if flush(h):
        a = sorted([val(h[0][0]),val(h[1][0]),val(h[2][0]),val(h[3][0]),val(h[4][0])])
        a.reverse
        return 6*13 + a[0] + a[1]/13. + a[2]/169. + a[3]/169./13. + a[4]/169./169.
    if straight(h):
       if h[0][0] == '2': return 5*13+0
       if h[0][0] == '3': return 5*13+1
       if h[0][0] == '4': return 5*13+2
       if h[0][0] == '5': return 5*13+3
       if h[0][0] == '6': return 5*13+4
       if h[0][0] == '7': return 5*13+5
       if h[0][0] == '8': return 5*13+6
       if h[0][0] == '9': return 5*13+7
       if h[0][0] == 'A': return 5*13+8
    if trip(h)[0]:
        return 4*13 + val(trip(h)[1])
    if pair2(h)[0]:
        return 3*13 + val(pair2(h)[1])+ val(pair2(h)[2])/13.+ val(pair2(h)[3])/169.
    if pair(h)[0]:
        a = [val(pair(h)[2]), val(pair(h)[3]), val(pair(h)[4])]
        a.sort()
        a.reverse()
        return 2*13 + val(pair(h)[1])+ a[0]/13.+ a[1]/169.+ a[2]/169./13.
    a = sorted([val(h[0][0]),val(h[1][0]),val(h[2][0]),val(h[3][0]),val(h[4][0])])
    a.reverse()
    return 13 + a[0] + a[1]/13. + a[2]/13./13. + a[3]/13./13./13. + a[4]/13./13./13./13.
    
f = open('poker.txt')
p1 = 0
for line in f:
    h = line.split()
    h1 = sorted(h[0:5])
    h2 = sorted(h[5:])
    if eval(h1) > eval(h2):
            p1 += 1

print(p1)




print(time.clock() - start)
