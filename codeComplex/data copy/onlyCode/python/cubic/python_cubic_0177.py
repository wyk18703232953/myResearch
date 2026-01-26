N=int(input())
L=list(map(int,input().split()))

DP=[[-1]*N for i in range(N)]
for d in range(N):
    for s in range(N-d):
        e=s+d
        if s==e:
            DP[s][e]=L[s]
            continue
        for m in range(s,e):
            l=DP[s][m]
            r=DP[m+1][e]
            if l==r and l!=-1:
                DP[s][e]=max(DP[s][e],l+1)
DP2=[i+1 for i in range(N)]
for i in range(N):
    if DP[0][i]!=-1:
        DP2[i]=1
        continue
    for j in range(i):
        if DP[j+1][i]!=-1:
            DP2[i]=min(DP2[i],DP2[j]+1)
print(DP2[N-1])