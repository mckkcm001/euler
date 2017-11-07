import time
start = time.clock()

with open('matrix.txt','r') as f:
    b = [[int(i) for i in r.split(',')] for r in f.readlines()]
'''
b =[
[131,673,234,103,18],
[201,96,342,965,150],
[630,803,746,422,111],
[537,699,497,121,956],
[805,732,524,37,331]
]
'''
'''
for i in b:
    print i   
print
'''
start = time.clock()
n = len(b)
for i in range(1,n):
    b[i][0] += b[i-1][0]
'''    
for i in b:
    print i   
print
'''    
for i in range(1,n):
    b[0][i] += b[0][i-1]
''' 
for i in b:
    print i
print
'''    
for i in range(1,n):
    b[i][i] += max(b[i-1][i], b[i][i-1])
    for j in range(i+1,n):
        b[i][j] += max(b[i-1][j], b[i][j-1])
        b[j][i] += max(b[j-1][i], b[j][i-1])
'''
for i in b:
    print i
print
'''  
print(time.clock() - start)  
print(b[n-1][n-1])            

print(time.clock() - start)
