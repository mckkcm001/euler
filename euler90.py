from itertools import combinations
import time
start = time.time()

s = set()
for i in combinations('0123456789',6):
    for j in combinations('0123456789',6):
        if (('0' in i and '1' in j or
             '0' in j and '1' in i)     and
            ('0' in i and '4' in j or
             '0' in j and '4' in i)     and
            ('0' in i and '9' in j or
             '0' in j and '9' in i or
             '0' in i and '6' in j or
             '0' in j and '6' in i)     and
            ('1' in i and '6' in j or
             '1' in j and '6' in i or
             '1' in i and '9' in j or
             '1' in j and '9' in i)     and
            ('2' in i and '5' in j or
             '2' in j and '5' in i)     and
            ('3' in i and '6' in j or
             '3' in j and '6' in i or
             '3' in i and '9' in j or
             '3' in j and '9' in i)     and
            ('4' in i and '9' in j or
             '4' in j and '9' in i or
             '4' in i and '6' in j or
             '4' in j and '6' in i)     and
            ('6' in i and '4' in j or
             '6' in j and '4' in i or
             '9' in i and '4' in j or
             '9' in j and '4' in i)     and
            ('8' in i and '1' in j or
             '8' in j and '1' in i)
            ):
                 s.add((i,j))
for i in s:
    print i                 
print len(s) /2          
                
    
print(time.time() - start)        

