import time
start = time.time()
n = 0
for p200 in range(0,201,200):
    for p100 in range(0,201,100):
        for p50 in range(0,201,50):
            for p20 in range(0,201,20):
                for p10 in range(0,201,10):
                    for p5 in range(0,201,5):
                        for p2 in range(0,201,2):
                            for p1 in range(0,201,1):
                                if p1+p2+p5+p10+p20+p50+p100+p200 > 200:
                                    break
                                if p1+p2+p5+p10+p20+p50+p100+p200 == 200:
                                    n += 1
                                    
                        
print(n)
print time.time() - start 