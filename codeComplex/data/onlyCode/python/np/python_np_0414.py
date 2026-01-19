import os, sys, atexit
from io import BytesIO, StringIO
 
input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
_OUTPUT_BUFFER = StringIO()
sys.stdout = _OUTPUT_BUFFER
 
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

n, m = map(int, input().split())
arr = [0] * n
for i in range(n):
    temp = list(map(int, input().split()))
    arr[i] = temp
x = 1
N = 2 ** m - 1
lo = 1
hi = 1000000009
ind = [0, 0]
while 1:
    l = {}
    freq = [0] * (2 ** m)
    for i in range(n):
        an = 0
        for j in range(m):
            if arr[i][j] >= x: an += 2 ** (m - j - 1)
        if freq[an] == 0:
            l[i] = an
        freq[an] = 1
    # print(l)
    ch = 0
    for k1, v1 in l.items():
        for k2, v2 in l.items():
            # if v1 == v2: continue
            if v1 | v2 == N:
                ch = 1
                ind[0] = k1 + 1
                ind[1] = k2 + 1
                # print(x)
                break
        if ch: break
    if ch:
        lo = x
        x = x * 2
    else:
        hi = x
        break
ans = lo
while hi - lo > 1:
    x = (lo + hi) // 2
    l = {}
    freq = [0] * (2 ** m)
    for i in range(n):
        an = 0
        for j in range(m):
            if arr[i][j] >= x: an += 2 ** (m - j - 1)
        if freq[an] == 0:
            l[i] = an
        freq[an] = 1
    # print(l)
    ch = 0
    for k1, v1 in l.items():
        for k2, v2 in l.items():
            # if v1 == v2: continue
            if v1 | v2 == N:
                ch = 1
                ind[0] = k1 + 1
                ind[1] = k2 + 1
                # print(x)
                break
        if ch: break
    if ch:
        lo = x
    else:
        hi = x
ans = lo
# print(ans)
if ind[0] == 0: print("1 1")
else: print(*ind)