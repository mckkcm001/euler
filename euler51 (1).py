import itertools

def is_prime(n):
    if n%2 == 0: return False
    for i in range(3,int(n**.5)+1,2):
        if n%i == 0: return False
    return True

d1 = [1,2,3,4,5,6,7,8,9]
d2 = [0,1,2,3,4,5,6,7,8,9]
d3 = [0,1,2,3,4,5,6,7,8,9]
d4 = [0,1,2,3,4,5,6,7,8,9]
d5 = [0,1,2,3,4,5,6,7,8,9]

m = 0
for i in itertools.product(d1,d2):
    
    if is_prime(10*i[0]+i[1]):
        print(i)

    
    
