n=int(input())
arr=list(map(int,input().split()))
dp=[[-1 for i in range(5+1)] for j in range(n)]
for i in range(1,6):
    dp[0][i] =1
for i in range(1,n):
    if arr[i] > arr[i - 1]:
        for j in range(1,6):
            for k in range(1,j):
                if dp[i-1][k]==1:
                    dp[i][j] =1
                    break
    elif arr[i] <arr[i-1]:
        for j in range(1,6):
            for k in range(j+1,6):
                if dp[i-1][k] ==1:
                    dp[i][j]=1
                    break
    else:
        for j in range(1,6):
            for k in range(1,6):
                if j ==k:
                    continue
                if dp[i-1][k] ==1:
                    dp[i][j] =1
                    break
ans=[]
for i in range(1,6):
    if dp[n-1][i]==1:
        ans.append(i)
        break
if len(ans) ==0:
    print(-1)
    exit()
for i in range(n-2,-1,-1):
    curr=ans[-1]
    if arr[i] >arr[i+1]:
        for j in range(curr+1,6):
            if dp[i][j] ==1:
                ans.append(j)
                break
    elif arr[i] <arr[i+1]:
        for j in range(1,curr):
            if dp[i][j] ==1:
                ans.append(j)
                break
    else:
        for j in range(1,6):
            if j ==curr:
                continue
            if dp[i][j] ==1:
                ans.append(j)
                break
ans=ans[::-1]
print(*ans)
