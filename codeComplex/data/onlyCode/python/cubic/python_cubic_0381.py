"""
DP
There are 2**(K-1) ways I can turn on a segment of K computers manually only

"""

N, MOD = map(int,input().split())

dp = []
comps = [0]*(N+1)

ncr = [[1]]
for i in range(420):
    tmp = [1]
    for j in range(i):
        tmp.append((ncr[i][j] + ncr[i][j+1]) % MOD)
    tmp.append(1)
    ncr.append(tmp)

for i in range(N):
    curr = list(comps)
    curr[1] = pow(2,i,MOD)
    for j in range(i - 1):
        m = pow(2,i - j - 2)
        for k in range(N):
            num = j - k + 2
            if num < 0: continue
            mr = (m * ncr[i - j - 1 + num][num]) % MOD
            curr[k + 1] += mr * dp[j][k]
            curr[k + 1] %= MOD
    dp.append(curr)

print(sum(dp[-1]) % MOD)