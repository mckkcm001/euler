import time
start = time.time()

a=[]
for n in range(256,512):
    a.append(str(bin(n))[3:])
    
s=0
for i in a:
    if i[0] == '1' and i[1] == '1':
        s+=1
    if i[0] == '1' and i[3] == '1':
        s+=1
    if i[1] == '1' and i[2] == '1':
        s+=1
    if i[1] == '1' and i[4] == '1':
        s+=1
    if i[2] == '1' and i[5] == '1':
        s+=1
    if i[5] == '1' and i[4] == '1':
        s+=1
    if i[4] == '1' and i[3] == '1':
        s+=1
    if i[4] == '1' and i[7] == '1':
        s+=1
    if i[3] == '1' and i[6] == '1':
        s+=1
    if i[6] == '1' and i[7] == '1':
        s+=1
    
print s

print time.time() - start