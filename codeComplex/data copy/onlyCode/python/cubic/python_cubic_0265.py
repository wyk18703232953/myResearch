def solve(i, j, k):
    if dp[i][j][k]!=-1:
        return dp[i][j][k]
    call = 0
    if i>0 and j>0:
        call = max(call, R[i]*G[j]+solve(i-1, j-1, k))
    if j>0 and k>0:
        call = max(call, G[j]*B[k]+solve(i, j-1, k-1))
    if k>0 and i>0:
        call = max(call, B[k]*R[i]+solve(i-1, j, k-1))
    dp[i][j][k] = call
    return call


nr, ng, nb = map(int,input().split())
R = [0]+list(map(int,input().split()))
G = [0]+list(map(int,input().split()))
B = [0]+list(map(int,input().split()))
R.sort()
G.sort()
B.sort()
dp = [[[-1]*(nb+1) for j in range(ng+1)] for i in range(nr+1)]
ans = solve(nr, ng, nb)
print(ans)