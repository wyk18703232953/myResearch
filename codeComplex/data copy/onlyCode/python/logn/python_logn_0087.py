import math


a, b = [int(x) for x in input().split()]
while a != 0 and b != 0:
    x = int(math.log(a, 2))
    y = int(math.log(b, 2))
    if x != y:
        break
    a = a & (~(1 << x))
    b = b & (~(1 << y))

if a == 0 and b == 0:
    print(0)
else:
    if b > a:
        a, b = b, a
    x = int(math.log(a, 2)) + 1
    b = (1 << x) - 1
    a = a | b
    print(a)
