import time
import math
import random

start = time.time()

def primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}  

    # The running integer that's checked for primeness
    q = 2  

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q        
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1
n=10
p = []
for i in primes():
    if i > math.pow(10,n/2.)+1: 
        break
    p.append(i)
    
print len(p)   

M={}
N={}
S={}

def is_prime(n):
    for i in p:
        if i > math.sqrt(n)+1:
            break
        if n%i == 0:
            return False
    return True

def FermatPrimalityTest(number):
    ''' if number != 1 '''
    if (number > 1):
        ''' repeat the test few times '''
        for time in range(3):
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = random.randint(2, number)-1
            
            ''' Test if a^(n-1) = 1 mod n '''
            if ( pow(randomNumber, number-1, number) != 1 ):
                return False
        
        return True
    else:
        ''' case number == 1 '''
        return False 

def MillerRabinPrimalityTest(number):
    '''
    because the algorithm input is ODD number than if we get
    even and it is the number 2 we return TRUE ( spcial case )
    if we get the number 1 we return false and any other even 
    number we will return false.
    '''
    if number == 2:
        return True
    elif number == 1 or number % 2 == 0:
        return False
    
    ''' first we want to express n as : 2^s * r ( were r is odd ) '''
    
    ''' the odd part of the number '''
    oddPartOfNumber = number - 1
    
    ''' The number of time that the number is divided by two '''
    timesTwoDividNumber = 0
    
    ''' while r is even divid by 2 to find the odd part '''
    while oddPartOfNumber % 2 == 0:
        oddPartOfNumber = oddPartOfNumber / 2
        timesTwoDividNumber = timesTwoDividNumber + 1 
     
    '''
    since there are number that are cases of "strong liar" we 
    need to check more then one number
    '''
    for time in range(3):
        
        ''' choose "Good" random number '''
        while True:
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = random.randint(2, number)-1
            if randomNumber != 0 and randomNumber != 1:
                break
        
        ''' randomNumberWithPower = randomNumber^oddPartOfNumber mod number '''
        randomNumberWithPower = pow(randomNumber, oddPartOfNumber, number)
        
        ''' if random number is not 1 and not -1 ( in mod n ) '''
        if (randomNumberWithPower != 1) and (randomNumberWithPower != number - 1):
            # number of iteration
            iterationNumber = 1
            
            ''' while we can squre the number and the squered number is not -1 mod number'''
            while (iterationNumber <= timesTwoDividNumber - 1) and (randomNumberWithPower != number - 1):
                ''' squre the number '''
                randomNumberWithPower = pow(randomNumberWithPower, 2, number)
                
                # inc the number of iteration
                iterationNumber = iterationNumber + 1
            '''     
            if x != -1 mod number then it because we did not found strong witnesses
            hence 1 have more then two roots in mod n ==>
            n is composite ==> return false for primality
            '''
            if (randomNumberWithPower != (number - 1)):
                return False
            
    ''' well the number pass the tests ==> it is probably prime ==> return true for primality '''
    return True 
    
for i in range(10):
    M[n,i]=0
    N[n,i]=0
    S[n,i]=0
    
c = int(math.pow(10,n-1))
while c < math.pow(10,n) :
    c+=1
    if c%2 == 0 or c%3 == 0 or c%5 == 0 or c%7 == 0 or c%11 == 0 or c%13 == 0 or c%17 == 0 or c%19 == 0 or c%23 == 0:
        continue
    if  FermatPrimalityTest(c):
        for x in range(10):
            if str(c).count(str(x)) == M[n,x]:
                N[n,x]+=1
                S[n,x]+=c
            if str(c).count(str(x)) > M[n,x]:
                M[n,x] = str(c).count(str(x)) 
                N[n,x]= 1
                S[n,x]= c
            
for x in range(10):
    print x,M[n,x],N[n,x],S[n,x]
        
print sum(S.values())
print time.time() - start        