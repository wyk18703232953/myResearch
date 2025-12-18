dp=[]
n,k=map(int,input().split())
for _ in range(n):
    p,t=map(int,input().split())
    dp.append((p,-t))
dp.sort(reverse=True)
print(dp.count(dp[k-1]))