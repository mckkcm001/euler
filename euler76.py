import time
start = time.clock()

def dig2(n):
    s = []
    for i in range(n-1,0,-1):
        s.append([i,n-i])
    return s
 
def dign(n):     
        s=[]
        t = dig2(n)
        for i in t:
            if i[0] >= i[1]:
                s.append(i)
                if i[1] > 1:
                    for j in diga[i[1]]:
                        s.append([i[0]]+j)
            else:
                for j in diga[i[1]]:
                    if j[0] > i[0]: 
                        continue
                    s.append([i[0]]+j)
        return s
         
diga = { 0 :  [[0]], 1:  [[1]],  2: [[1,1]], 3:  [[2,1],[1,1,1]],
         4:  [[3,1],[2,2],[2,1,1],[1,1,1,1]]   }

for i in range(5,101):        
    diga[i] = dign(i)
    print(i,len(diga[i]))

print(time.clock() - start)