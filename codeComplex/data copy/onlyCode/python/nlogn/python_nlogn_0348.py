from collections import defaultdict

n, a = int(input()), [int(x) for x in input().split()]
pow2 = [1 << i for i in range(32)]
mp = defaultdict()
for x in a:
    mp[x] = 1
mxSiz = 1
ans = [a[0]]
for x in a:
    for y in pow2:
        if x-y in mp and x+y in mp:
            mxSiz = 3
            ans = [x-y, x, x+y]
        if x-y in mp and 2 > mxSiz:
            mxSiz = 2
            ans = [x-y, x]

print(mxSiz)
print(*ans)
