from sys import stdin,stdout
from itertools import accumulate
nmbr = lambda: int(stdin.readline())
lst = lambda: list(map(int,stdin.readline().split()))
for _ in range(1):#nmbr()):
    n,k=lst()
    a=lst()
    a.sort()
    s = set()
    for v in a:
        if (v % k != 0) or v // k not in s:
            s.add(v)
    print(len(s))