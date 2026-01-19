import sys

II = {1 << i: i for i in range(20)}

def build_input(n):
    if n <= 0:
        N = 0
        K = 1
        S = []
        return N, K, S
    K = max(1, n % 5 + 1)
    N = K * n
    S = []
    for i in range(N):
        if (i + n) % (K + 1) == 0:
            S.append(-1)
        else:
            S.append((i * 3 + n) % K)
    return N, K, S

def calc(N, K, S, mmm):
    inf = 300000
    X = [[0] * N for _ in range(K)]
    for k in range(K):
        Xk = X[k]
        mi = inf
        r = 0
        for i in range(N - 1, -1, -1):
            if S[i] < 0 or S[i] == k:
                r += 1
            else:
                r = 0
            if r >= mmm:
                if i + mmm < mi:
                    mi = i + mmm
            Xk[i] = mi

    Y = [0] * (1 << K)
    for i in range(1, 1 << K):
        mi = inf
        for j in range(K):
            if (i >> j) & 1:
                ii = i ^ (1 << j)
                if Y[ii] < N:
                    if X[j][Y[ii]] < mi:
                        mi = X[j][Y[ii]]
        Y[i] = mi
    return 1 if Y[-1] < inf else 0

def main(n):
    N, K, S = build_input(n)
    if N == 0 or K == 0:
        print(0)
        return
    l, r = 0, N // K + 1
    while r - l > 1:
        m = (l + r) >> 1
        if calc(N, K, S, m):
            l = m
        else:
            r = m
    print(l)

if __name__ == "__main__":
    main(10)