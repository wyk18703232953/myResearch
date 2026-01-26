n, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
s = set(a)
mv = 999
if len(s) < n:
    print(0)
else:
    for i in a:
        if i & x != i and i & x in s:
            print(1)
            break
    else:
        k = [i & x for i in a]
        if len(set(k)) < n:
            print(2)
        else:
            print(-1)
