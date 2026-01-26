from copy import deepcopy
def sol(n,m,k,aa,bb):
    if k&1:
        return [[-1] * m] * n
    ans = [[float('inf')]*(m+2) for _ in range(n+2)]
    k >>= 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            ans[i][j] = min(aa[i][j], aa[i][j-1], bb[i][j], bb[i-1][j])
    for _ in range(k-1):
        oans = deepcopy(ans)
        for i in range(1,n+1):
            for j in range(1,m+1):
                ans[i][j] = min(
                    aa[i][j]+oans[i][j+1],
                    aa[i][j-1]+oans[i][j-1],
                    bb[i][j]+oans[i+1][j],
                    bb[i-1][j]+oans[i-1][j])

    ans = ans[1:-1]
    ans = [x[1:-1] for x in ans]
    ans = [[2*x for x in a] for a in ans]
    return ans

n,m,k = map(int, input().split())
aa = [list(map(int, input().split())) for _ in range(n)]
inf = float('inf')
bb = [list(map(int, input().split())) for _ in range(n-1)]
aa = [[inf, *x, inf] for x in aa]
bb = [[inf, *x, inf] for x in bb]
pad = [inf] * (m+1)
aa = [pad, *aa, pad]
pad = [inf] * (m+2)
bb = [pad, *bb, pad]
ans = sol(n,m,k,aa,bb)
print('\n'.join(' '.join(map(str, a)) for a in ans))
