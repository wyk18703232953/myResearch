n,m,k=[int(x) for x in input().split()]
left=[];right=[]
for i in range(n):
    temp=[int(x) for x in input().split()]
    left.append(temp)
for i in range(n-1):
    temp=[int(x) for x in input().split()]
    right.append(temp)
dp_old=[[0 for x in range(m)] for x in range(n)]
if k%2!=0:
    for i in range(n):
        print(*[-1 for x in range(m)])
else:
    k//=2
    for k1 in range(k):
        dp=[[0 for x in range(m)] for x in range(n)]
        for row in range(n):
            for col in range(m):
                t=float("inf")
                if 0<col:
                    t=min(t,dp_old[row][col-1]+2*left[row][col-1])
                if m-1>col:
                    t=min(t,dp_old[row][col+1]+2*left[row][col])
                if 0<row:
                    t=min(t,dp_old[row-1][col]+2*right[row-1][col])
                if n-1>row:
                    t=min(t,dp_old[row+1][col]+2*right[row][col])
                dp[row][col]=t
        for row in range(n):
            for col in range(m):
                dp_old[row][col]=dp[row][col]
    for i in range(n):
        print(*dp_old[i])