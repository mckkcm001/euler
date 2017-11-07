def dec(n):
    rem=[]
    num = 10
    rem.append(num%n)
    num = (num%n)*10
    for i in range(n):
       if num%n in rem:
           return len(rem)
       else:
          rem.append(num%n)
          num = (num%n)*10
max = 0
n = 0
for i in range(1,1000):
    if dec(i) > max:
        max = dec(i)
        n = i

print(n, max)


