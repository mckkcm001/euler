def pald(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i:i+1] != n[len(n)-1-i:len(n)-i]:
            return False
    return True

def palb(n):
    n = str(n)[2:]
    for i in range(len(n)//2): 
        if n[i:i+1] != n[len(n)-1-i:len(n)-i]:
            return False
    return True

n = []
for i in range(1000000):
    if pald(i) and palb(bin(i)):
        n.append(i)
        
print(sum(n))
