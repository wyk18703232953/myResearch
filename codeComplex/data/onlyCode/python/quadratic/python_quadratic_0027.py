n = int(input())
s = [input() for i in range(n)]
MOD = 10**9 + 7

dps = [[0]*(n + 3) for i in range(n + 1)]
dpf = [[0]*(n + 3) for i in range(n + 1)]

for k in range(n + 1):
    dps[0][k] = 1

for pos, char in enumerate(s):
    if char == "s":
        #dps[pos + 1][depth] = dps[pos][depth]  + .... + dps[pos][pos] + dpf[pos][depth]
        for depth in range(pos + 2):
            dps[pos + 1][depth] = dpf[pos][depth] - \
                dpf[pos][depth - 1] + dps[pos][pos] - dps[pos][depth - 1]
            #sum(dps[pos][k] for k in range(depth, pos + 1))

            dps[pos + 1][depth] += dps[pos + 1][depth - 1]
            dps[pos + 1][depth] %= MOD

        for p in range(pos + 2, n+1):
            dpf[pos + 1][p] += dpf[pos + 1][p - 1]
            dpf[pos + 1][p] %= MOD
        continue

    else:
        #dpf[pos + 1][depth] =  dpf[pos][depth - 1] + dps[pos][depth - 1] + .......... + depth[pos][pos]
        #dps[pos + 1][depth] = impossible
        for depth in range(1, pos + 2):
            dpf[pos + 1][depth] = dpf[pos][depth - 1] - \
                dpf[pos][depth - 2] + dps[pos][pos] - dps[pos][depth - 2]
            #sum(dps[pos][k] for k in range(depth - 1, pos + 1))
            dpf[pos + 1][depth] += dpf[pos + 1][depth - 1]
            dpf[pos + 1][depth] %= MOD
        for p in range(pos + 2, n+1):
            dpf[pos + 1][p] += dpf[pos + 1][p - 1]
            dpf[pos + 1][p] %= MOD


ans = dps[n][n] % MOD
print(ans)
