import time

start = time.time()
  
c=0
for n1 in range(9,-1,-1):
    for n2 in range(n1,-1,-1):
        for n3 in range(n2,-1,-1):
            for n4 in range(n3,-1,-1):
                for n5 in range(n4,-1,-1):
                    for n6 in range(n5,-1,-1):
                        c+=1
                        print n1,n2,n3,n4,n5,n6
for n1 in range(10):
    for n2 in range(n1,10):
        for n3 in range(n2,10):
            for n4 in range(n3,10):
                for n5 in range(n4,10):
                    for n6 in range(n5,10):
                        c+=1  
                        print n1,n2,n3,n4,n5,n6
                        
print c

print(time.time() - start)
