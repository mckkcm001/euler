import time
import operator
#from itertools import combinations, permutations

start = time.time()

d = {} 
dd = {}
for i in range(20):
    d['S'+str(i+1)]=i+1
    d['D'+str(i+1)]=2*(i+1) 
    dd['D'+str(i+1)]=2*(i+1)
    d['T'+str(i+1)]=3*(i+1) 
d['S25']=25
d['D25']=50
dd['D25']=50
#d['S0']=0     
    
#sorted_d = sorted(d.iteritems(), key=operator.itemgetter(1))
#sorted_dd = sorted(dd.iteritems(), key=operator.itemgetter(1))
    
turn = {}
for i in dd:
    turn[(i,)]=dd[i]

for i in d:
    for j in dd:
        turn[(i,j)]=d[i]+dd[j]
            
for i in d:
    for j in d:
        for k in dd:
            if i < j:
                turn[(i,j,k)]=d[i]+d[j]+dd[k]
            else:
                turn[(j,i,k)]=d[i]+d[j]+dd[k]
            
checkout = {i:turn[i] for i in turn if turn[i] < 100}

print checkout
'''
for l in range(1,4): 
    for k in ['D','S','T']:      
        for i in sorted_checkout:
            if len(i[0]) == l and i[0][0][0] == k:
                print i
'''
print len(turn),len(checkout)            
print time.time() - start        