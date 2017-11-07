def abundant(n):
    a = []
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            a.append(i)
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s > n

def abundantList(n):
    a = []
    for i in range(1,n):
        if abundant(i):
            a.append(i)
    return a

alist = abundantList(29000)

def abundantSum(n):
    for a in alist:
        if a > n:
            break
        for b in alist:
            if b > n:
                break
            if a + b == n:
                return True
    return False      
    
def nonAbundantSum(n):
    s = 0
    for i in range(n):
        if abundantSum(i)==False:
            s += i           
    return s  

print(nonAbundantSum(100))
