n = []
def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
    
for i in range(1000000):
    s = 0
    #print(str(i)+' ', end="")
    for j in str(i):
        #print(j+' ', end="")
        s += fact(int(j))
    #print(s)
    if s == i:   
        n.append(i)
print(n)
