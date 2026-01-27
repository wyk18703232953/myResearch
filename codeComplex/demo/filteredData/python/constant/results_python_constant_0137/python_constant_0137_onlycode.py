import math
a, b = map(int, input().split())
if a % b == 0:
    print(int(a/b))
else:
    c = 0
    while b:
        c += a//b
        temp = a
        a = b
        b = temp % b
    print(c)
