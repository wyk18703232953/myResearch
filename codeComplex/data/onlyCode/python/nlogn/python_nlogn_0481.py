n, m = map(int, input().split())
A = list(map(int, input().split()))
from collections import Counter
C = Counter(A)

def is_ok(x):
    cnt = 0
    for v in C.values():
        cnt += v//x
    if cnt >= n:
        return True
    else:
        return False


ok = 0
ng = 1000
while ok+1 < ng:
    c = (ok+ng)//2
    if is_ok(c):
        ok = c
    else:
        ng = c
print(ok)
