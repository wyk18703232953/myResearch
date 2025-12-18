N = int(input())
X = list(map(int, input().split()))
from collections import defaultdict
dp1 = defaultdict(lambda :-1)
M=1001
def ec(i,j):
    return i*M+j

for i in range(N):
    dp1[ec(i,i+1)] = X[i]
for i in range(2, N+1):
    for j in range(N-i+1):
        for k in range(1, i):
            u, v = dp1[ec(j,j+k)], dp1[ec(j+k,j+i)]
            if u != -1 and v != -1 and u == v:
                dp1[ec(j,j+i)] = u+1
                break

dp2 = [0]*(N+1)
for i in range(N):
    dp2[i+1] = dp2[i]+1
    for j in range(i+1):
        if dp1[ec(j,i+1)] == -1:
            continue
        dp2[i+1] = min(dp2[i+1], dp2[j]+1)
print(dp2[-1])
