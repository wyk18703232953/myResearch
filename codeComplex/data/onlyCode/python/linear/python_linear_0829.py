def matches(pos, c, case):
    if case==0:
        return pos%3=="RGB".index(c)
    elif case==1:
        return pos%3=="GBR".index(c)
    else:
        return pos%3=="BRG".index(c)

q = int(input())
for _ in range(q):
    n, k = map(int, input().split())

    s = input()

    mglobal = k

    r=g=b=0

    for i, c in enumerate(s[:k]):
            
        r += not matches(i, c, 0)
        g += not matches(i, c, 1)
        b += not matches(i, c, 2)
    
    mglobal = min([mglobal, r, g, b])
    for i, c in enumerate(s[k:]):
        i+=k
        r += -(not matches(i-k, s[i-k], 0)) + (not matches(i, c, 0))    
        g += -(not matches(i-k, s[i-k], 1)) + (not matches(i, c, 1))    
        b += -(not matches(i-k, s[i-k], 2)) + (not matches(i, c, 2))    
    
        mglobal = min([mglobal, r, g, b])

    print(mglobal)
