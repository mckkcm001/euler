import math

def isPrime(number):
    if number == 2:
        return True
    if number < 0:
        number *= -1
    if number % 2 == 0:
       return False
    count = int(math.sqrt(number))
    for x in range (3, count+1, 2):
        if number % x == 0:
            return False
    else:
        return True

def getMaxFactor(number):
    count = number/2
    while count > 0:
        if number % count == 0:
            return count
        count -= 1

def factors(number):
    l = [getMaxFactor(number)]
    l.append(number/l[0])
    while True:
        if not isPrime(l[0]):
            high = getMaxFactor(l[0])
            low = l[0]/high
            del l[0]
            l = [low] + l
            l = [high] + l
        else:
            break
    l.sort()
    return l

    
print factors(15),factors(14)
print factors(20),factors(21)
print
print factors(85),factors(84)
print factors(119),factors(120)
print
print factors(493),factors(492)
print factors(696),factors(697)
print
print factors(16731),factors(16730)
print factors(23660),factors(23661)
print
print factors(97513),factors(97512)
print factors(137903),factors(137904)
print
print factors(568345),factors(568344)
print factors(803760),factors(803761)
print
print factors(3312555),factors(3312554)
print factors(4684659),factors(4684660)
print
print factors(707106802629L),factors(707106802628L)
print factors(1000000030324L),factors(1000000030323L)
