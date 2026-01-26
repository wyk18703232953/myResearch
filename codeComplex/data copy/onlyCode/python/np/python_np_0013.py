n = int(input())
probs = list()
for i in range(n): probs.append(list(map(float, input().split())))
dp = [list([0 for i in range(1<<n)]) for i in range(n)]
dp[0][(1<<n)-1] = 1
ak = [list() for i in range(n+1)]
for i in range(1<<n):
    ak[bin(i).count("1")].append(i)
for k in range(1, n):
    for ele in ak[n-k+1]:
        for j in range(n):
            if (ele&(1<<j)):
                for w in range(n):
                    if (ele&(1<<w)) and j != w:
                        dp[k][ele-(1<<j)] += (dp[k-1][ele]*probs[w][j])/(((n-k+1)*(n-k))/2)
for i in range(n):
    print(dp[n-1][(1<<i)], end = " ")
print()