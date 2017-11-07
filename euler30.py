n = set()
for d100000 in range(5):
    for d10000 in range(10):
        for d1000 in range(10):
            for d100 in range(10):
                for d10 in range(10):
                    for d1 in range(10):
                        if d100000*100000+d10000*10000+d1000*1000+d100*100+d10*10+d1==d100000**5+d10000**5+d1000**5+d100**5+d10**5+d1**5:
                            n.add(d100000*100000+d10000*10000+d1000*1000+d100*100+d10*10+d1)
print(n,sum(n))
