import sys
input=sys.stdin.readline

mod=10**9+7
n,t=map(int,input().split())
a=[] #Denote song number by it's index in this list
for i in range(n):
    time,genre=map(int,input().split())
    genre-=1 #converting to 0-based indexing
    a.append((time,genre))
dp=[[0 for j in range(3)] for i in range(1<<n)] #dp[permuation of song][last genre of that permutation]
for i in range(n):
    dp[1<<i][a[i][1]]=1
for i in range(1<<n):
    for j in range(3):
        if(dp[i][j]==0):
            continue
        mask=1 #Will correspond to the kth bit, i.e 1<<k for each iteration, for the case of including the kth song 
        for k in range(n):
            if(i&mask or a[k][1]==j): #as we are not allowed to repeat same song or have same genre successively
                mask<<=1
                continue
            dp[i|mask][a[k][1]]=(dp[i|mask][a[k][1]]+dp[i][j])%mod
            mask<<=1
ans=0
for i in range(1<<n):
    mask=1
    duration=0
    for j in range(n):
        if(i&mask):
            duration+=a[j][0]
        mask<<=1
    if(duration==t):
        ans=(ans+sum(dp[i]))%mod
print(ans)
            
        
    
        
    
    