def is_pan(n):
    if set(str('123456789')) == set(str(n)):
        return True
    return False
        
def concat(n,s):
    a = ''
    for i in s:
        a += str(n*i)
    if len(a) == 9 and is_pan(int(a)):
        return [True,int(a)]
    return [False,0]
max = 0
for i in range(1,100000):
    s = []
    for j in range(1,10):
        s.append(j)
        if concat(i,s)[0]:
            if concat(i,s)[1] > max:
                max = concat(i,s)[1]

print(max)

         
        
