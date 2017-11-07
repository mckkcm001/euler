import time
start = time.time()


for x in range(1,24):
    a=[]
    for n in range(256,256+2**x):
        b = '0'+str(bin(n))[3:]+'0'
        if '010' in b: 
            continue
        if '0110' in b:
            continue
        a.append(str(bin(n))[3:])
        
    print x,len(a)


print time.time() - start