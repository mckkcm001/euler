import time
start = time.clock()

for i1 in '0123456789':
    for i2 in '0123456789':
        print i2
        for i3 in '0123456789':
            for i4 in '0123456789':
                for i5 in '0123456789':
                    for i6 in '0123456789':
                        for i7 in '0123456789':
                            for i8 in '0123456789':
                                for i9 in '0123456789':
                                    a = ('1' + i1 + '2' + i2 + '3' + i3 +
                                         '4' + i4 + '5' + i5 + '6' + i6 +
                                         '7' + i7 + '8'+ i8 + '9' +i9 + '0')
                                     
                                    s = (int(a))**.5
                                    #print a, int(a), s
                                    if s == int(s):
                                        print s
                                        break
print(time.clock() - start)                
              