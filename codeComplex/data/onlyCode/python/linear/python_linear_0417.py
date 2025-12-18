n,x = list(map(int, input().split()))
a = set(map(int, input().split()))

if len(a) < n :
    print(0)
else :
    d = set()
    p = 0
    for i in a :
        d.add(i&x)
        if i&x != i and i&x in a :
            print(1)
            p = 1
            break
    if len(d) < n and p == 0 :
        print(2)
    elif p != 1 :
        print(-1)
