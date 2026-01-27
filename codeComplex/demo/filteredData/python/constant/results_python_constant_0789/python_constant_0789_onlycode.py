import math
for _ in range (int(input())):
    n=int(input())
    s=1
    ch=0
    for i in range (1,31):
        s*=2
        d=math.sqrt(n//s)
        if n%s==0 and d==int(d):
            ch=1
            break
    if ch:
        print("YES")
    else:
        print("NO")