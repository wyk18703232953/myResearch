pfs=[i*i for i in range(1,3163)]
p=[i for i in range(0,10000001)]
for i in range(1,10000001):
    if(p[i]==i):
        for j in pfs:
            if(i*j>10000000): break
            p[i*j]=i
t=int(input())
for lll in range(0,t):
    n,k=map(int,input().split())
    zc=list(map(int,input().split()))
    s=[p[zc[i]] for i in range(0,len(zc))]
    dp=[n]*(k+1)
    dp[0]=1
    ys=[{}]*(n+1)
    for i in range(0,len(s)):
        for j in range(k,-1,-1):
            if(dp[j]==n): continue
            if(ys[j].get(s[i],-1)!=-1):
                if(j<k and dp[j]<dp[j+1]):
                    dp[j+1]=dp[j]
                    ys[j+1]=ys[j]
                dp[j]+=1
                ys[j]={}
            ys[j][s[i]]=1
    print(min(dp))