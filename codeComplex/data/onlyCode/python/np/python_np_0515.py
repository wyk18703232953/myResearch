import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
S = [-1 if a == "?" else ord(a) - 97 for a in input()]
II = {1 << i: i for i in range(20)}
def calc(mmm):
    inf = 300000
    X = [[0] * N for _ in range(K)]
    for k in range(K):
        Xk = X[k]
        mi = inf
        r = 0
        for i in range(N)[::-1]:
            if S[i] < 0 or S[i] == k:
                r += 1
            else:
                r = 0
            if r >= mmm:
                mi = min(mi, i + mmm)
            Xk[i] = mi

    Y = [0] * (1 << K)
    for i in range(1, 1 << K):
        mi = inf
        for j in range(K):
            if i >> j & 1:
                ii = i ^ (1 << j)
                if Y[ii] < N:
                    mi = min(mi, X[j][Y[ii]])
        Y[i] = mi
    return 1 if Y[-1] < inf else 0
    
l, r = 0, N // K + 1
while r - l > 1:
    m = l + r >> 1
    if calc(m):
        l = m
    else:
        r = m
print(l)

