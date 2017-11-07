import time
start = time.clock()
a = ''

for i in range(200000):
  a += str(i)

print(int(a[1:2])*int(a[10:11])*int(a[100:101])*int(a[1000:1001])*int(a[10000:10001])*int(a[100000:100001])*int(a[1000000:1000001]))

print(time.clock() - start)
