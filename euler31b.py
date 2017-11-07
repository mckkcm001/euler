import time
start = time.time()
n = 0
tot = 256
a=[128,64,32,16,8,4,2,1]
for p200 in range(0, (tot//a[0])*a[0] + 1,a[0]):
    if p200 == tot:
            n += 1
            break
    for p100 in range(0,((tot-p200)//a[1])*a[1]+ 1,a[1]):
        if p100+p200 > tot:
            break
        if p100+p200 == tot:
            n += 1
            break
        for p50 in range(0,((tot-p200-p100)//a[2])*a[2]+ 1,a[2]):
            if p50+p100+p200 > tot:
                break
            if p50+p100+p200 == tot:
                n += 1
                break
            for p20 in range(0,((tot-p200-p100-p50)//a[3])*a[3]+ 1,a[3]):
                if p20+p50+p100+p200 > tot:
                    break
                if p20+ p50+p100+p200 == tot:
                    n += 1
                    break
                for p10 in range(0,((tot-p200-p100-p50-p20)//a[4])*a[4]+ 1,a[4]):
                    if p10+p20+p50+p100+p200 > tot:
                        break
                    if p10+p20+p50+p100+p200 == tot:
                        n += 1
                        break
                    for p5 in range(0,((tot-p200-p100-p50-p20-p10)//a[5])*a[5]+ 1,a[5]):
                        if p5+p10+p20+p50+p100+p200 > tot:
                            break
                        if p5+p10+p20+p50+p100+p200 == tot:
                            n +=1
                            break
                        for p2 in range(0,((tot-p200-p100-p50-p20-p10-p5)//a[6])*a[6]+ 1,a[6]):
                            if p2+p5+p10+p20+p50+p100+p200 > tot:
                                break
                            if p2+p5+p10+p20+p50+p100+p200 == tot:
                                n += 1
                                break
                            for p1 in range(0,((tot-p200-p100-p50-p20-p10-p5-p2)//a[7])*a[7]+ 1,a[7]):
                                if p1+p2+p5+p10+p20+p50+p100+p200 > tot:
                                    break
                                if p1+p2+p5+p10+p20+p50+p100+p200 == tot:
                                    n += 1
                                    break
                                    
                        
print(n)
print time.time() - start 