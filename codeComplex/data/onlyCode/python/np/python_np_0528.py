N, K = list(map(int, input().split()))
S = input().strip()
S = [-1 if _ == '?' else ord(_) - ord('a') for _ in S]

def check(x):
    p = [[N for i in range(N+1)] for k in range(K)]

    for k in range(K):
        keep = 0
        for i in range(N-1, -1, -1):
            keep += 1
            if S[i] != -1 and S[i] != k:
                keep = 0
            p[k][i] = p[k][i+1]
            if keep >= x:
                p[k][i] = i + x - 1

    d = [N for s in range(1<<K)]
    d [0] = -1
    for s in range(1, 1<<K):
        for k in range(K):
            if (s&(1<<k)) and (d[s^(1<<k)]<N):
                d[s] = min(d[s], p[k][d[s^(1<<k)]+1])
                # print('d[%d%d]=%d'%(s//2, s%2, d[s]))
    return d[(1<<K)-1] < N
    
l, r = 0, N//K

while l < r:
    mid = (l + r + 1) // 2
    if check(mid):
        l = mid
    else:
        r = mid - 1
print(l)
