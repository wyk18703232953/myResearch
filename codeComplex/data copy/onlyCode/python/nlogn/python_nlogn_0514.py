import sys
import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

t = int(input())
from collections import Counter
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    C = Counter(A)
    B = []
    for k, v in C.items():
        if v >= 4:
            B.append(k)
            B.append(k)
        elif v >= 2:
            B.append(k)
    #print(B)
    B.sort()
    l = len(B)
    m = 10**18
    ans = [-1, -1, -1, -1]
    for i in range(l-1):
        x, y = B[i], B[i+1]
        temp = (4*(x+y)**2)/(x*y)
        if temp < m:
            m = temp
            ans = [x, x, y, y]
    print(*ans)
