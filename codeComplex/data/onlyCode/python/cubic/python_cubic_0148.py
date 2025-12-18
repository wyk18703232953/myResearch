N = int(input())
X = list(map(int, input().split()))
from collections import defaultdict
dp = defaultdict(lambda :-1)
M=1000001
for i in range(N):
    dp[i+M] = X[i]
for i in range(2, N+1):
    for j in range(N-i+1):
        for k in range(1, i):
            u, v = dp[j+M*k], dp[j+k+M*(i-k)]
            if u == -1 or v == -1 or u != v:
                continue
            dp[j+M*i] = u+1;break


#print(dp)
dp2 = [0]*(N+1)
for i in range(N):
    dp2[i+1] = dp2[i]+1
    for j in range(i+1):
        if dp[j+(i+1-j)*M] == -1:
            continue
        dp2[i+1] = min(dp2[i+1], dp2[j]+1)
print(dp2[-1])
