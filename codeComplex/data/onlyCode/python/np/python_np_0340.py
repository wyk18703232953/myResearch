n,tnow=map(int,input().split())
left=int("".join(["1" for i in range(n)]),2)
arr=[]
dp={}
for i in range(n):
    a,b=map(int,input().split())
    arr.append([a,b])
def recur(tnow,prevgenre,left):
    key=str(left)+"_"+str(prevgenre)
    if tnow==0:
        return 1
    elif key in dp:
        return dp[key]
    else:
        ans=0
        for i in range(n):
            if (left&(1<<i))!=0:
                if arr[i][0]<=tnow and arr[i][1]!=prevgenre:
                    left=left&(~(1<<i))
                    ans+=recur(tnow-arr[i][0],arr[i][1],left)
                    left=left|(1<<i)
        dp[key]= ans
        return ans
       
print(recur(tnow,4,left)%(10**9+7))
