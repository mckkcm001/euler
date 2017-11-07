def problem23():
    
    def d(n):
    
        m, s = n ** 0.5, 1
        if m == int(m): s -= int(m)
        m = int(m//1) + 1
        for i in range(2, m):
            if n%i == 0: s += i + (n/i)
        return s
    
    a, s = set(), 0
    for i in range(1, 20612):
        if d(i) > i: a.add(i)
        if not any((i - j) in a for j in a): s += i
    return s

print(problem23())
