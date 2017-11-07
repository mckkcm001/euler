import time
start = time.time()

f1 = 1
f2 = 1
c = 2
while True:
    c += 1
    f3 = f2 + f1
    if sorted(str(f3)[-9:]) == sorted('123456789') and \
       sorted(str(f3)[0:9]) == sorted('123456789'):
        print c
        break
    f1 = f2
    f2 = f3
    
      
       
print(time.time() - start)        

