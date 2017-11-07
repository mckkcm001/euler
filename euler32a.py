import itertools

d = set([1,2,3,4,5,6,7,8,9])
a = set(itertools.permutations(d, 1))

p1 = set()
p2 = set()
p3 = set()

for m in a:
    for n in itertools.permutations(d.difference(set(m)),4):
        for o in itertools.permutations(d.difference(set(m)).difference(set(n)),4):
            if (1*m[0])*(1000*n[0]+100*n[1]+10*n[2]+n[3])==1000*o[0]+100*o[1]+10*o[2]+o[3]:
                p3.add(1000*o[0]+100*o[1]+10*o[2]+o[3])
                p1.add(1*m[0])
                p2.add(1000*n[0]+100*n[1]+10*n[2]+n[3])

print(sum(p3))

    
    
