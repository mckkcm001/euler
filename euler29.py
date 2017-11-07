n = set()
for a in range(2,101):
    for b in range(2,101):
        n.add(a**b)
print(len(n))
