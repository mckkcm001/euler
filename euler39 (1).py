def rt(i,j,k):
    if i*i+j*j == k*k:
        return True
    return False

t = set()
for i in range(1,500):
    for j in range(500,500-i,-1):
        for k in range(max(i,j),500):
            if rt(i,j,k):
                t.add(set([i,j,k]))


print(t)

         
        
