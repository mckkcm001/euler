def abundant(n):
    a = []
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            a.append(i)
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s > n

a = []
for i in range(22000):
    if abundant(i):
        a.append(i)

b = []   
for i in range(22000):
    t = []
    for j in range(len(a)):
        t.append(a[j])
        if a[j] > i/2:
            break
    tr = []
    n = a[len(t)-2:len(a)]
    for j in range(len(n)):
        tr.append(n[j])
        if n[j] > i:
            break
    tr.reverse()

    k = 0
    j = 0
    while(j < len(t) and k < len(tr)):
        if t[j] + tr[k] < i:
            j += 1
            continue
        if t[j] + tr[k] == i:
            b.append(i)
            break
        if t[j] + tr[k] > i:
            k += 1
c = [i for i in range(22000)]
for i in b:
    c.remove(i)
sum = 0
for i in c:
    sum += i
print(sum)
         
        
