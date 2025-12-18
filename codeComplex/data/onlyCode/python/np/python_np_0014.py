n=int(input())
b=[]
for i in range(n):
    b.append(list(map(float,input().split())))

ma=1<<n
dp=[0 for j in range(ma)]
dp[0]=1
for mask in range(1,ma):
    l=n-bin(mask).count("1")+1
    res=l*(l-1)//2
    for i in range(n):
        if mask&(1<<i):
            for j in range(n):
                if not mask&(1<<j):

                    dp[mask]+=((dp[mask^(1<<i)]*b[j][i])/res)


ans=[]
for i in range(n):
    ans.append(dp[ma-1-(1<<i)])
print(*ans)

