def isprime(n):
    for i in range(2,int(n**.5)+2):
        if n%i == 0:
            return False
    return True

m = 0
ma = 0
mb = 0

for a in range(-999,1000):
    for b in range(-999,1000):
        n = 0
        while n*n + a*n + b > 0 and isprime(n*n + a*n + b):
            n += 1
            if n > m:
                ma = a
                mb = b
                m = n
print(m,ma*mb)   
