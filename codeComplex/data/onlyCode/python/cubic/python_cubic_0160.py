import sys
dp=[]
a=[]
def calcdp(l,r):
    global dp,a
    if l+1==r :
        dp[l][r]=a[l]
        return dp[l][r]
    if dp[l][r]!=0:
        return dp[l][r]
    dp[l][r]=-1
    for k in range(l+1,r):
        la=calcdp(l,k)
        ra=calcdp(k,r)
        if la>0 and la==ra:
            dp[l][r]=la+1
    return dp[l][r]
def solve(n):
    dp2=[float('inf')]*(n+1)
    dp2[0]=0
    for i in range(n):
        for j in range(i+1,n+1):
            if calcdp(i,j)>0:
                dp2[j]=min(dp2[j],dp2[i]+1)
    #print(dp2,dp)
    return dp2[n]
def ip():
    global dp,a

    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    a.append(0)
    #a.append(0)
    dp=[]
    ll=[0]*(n+1)
    for _ in range(n+1):
        dp.append(list(ll))
    
    #calcdp(dp,0,n-1,a)
    print(solve(n))
    #print(dp)
ip()
    
    