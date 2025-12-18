# https://codeforces.com/contest/257/problem/A

n, m, k = list(map(int, input().split()))
f = list(map(int, input().split()))
f.sort()

fs = 0
ptr = len(f) - 1
while ptr >= 0:
    if m <= k:
        print(fs)
        exit()
    k -= 1
    k += f[ptr]
    fs += 1
    ptr -= 1

if m <= k:
    print(fs)
else:
    print(-1)