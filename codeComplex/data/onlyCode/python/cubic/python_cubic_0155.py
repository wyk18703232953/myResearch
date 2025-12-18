import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

DP=[[-1]*(n+1) for i in range(n+1)]
for i in range(n):
    DP[i][i]=A[i]

for mid in range(1,n):
    for i in range(n):
        j=i+mid
        if j==n:
            break
        for k in range(i,j+1):
            if DP[i][k]==DP[k+1][j] and DP[i][k]!=-1:
                DP[i][j]=DP[i][k]+1

ANS=[2000]*(n+1)
ANS.append(0)
for i in range(n):
    ANS[i]=min(ANS[i],ANS[i-1]+1)
    for j in range(i,n):
        if DP[i][j]!=-1:
            ANS[j]=min(ANS[j],ANS[i-1]+1)
            
print(ANS[n-1])
