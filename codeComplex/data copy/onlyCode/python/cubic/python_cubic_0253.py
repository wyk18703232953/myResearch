r,g, b = map(int,input().split())
R = sorted([*map(int,input().split())],reverse=True)
G= sorted([*map(int,input().split())],reverse=True)
B = sorted([*map(int,input().split())],reverse=True)
mem = [[[-1 for i in range(201)] for j in range(201)] for j in range(201)]
def dp(i,j,k):
    p = (i==r)+(j==g)+(k==b)
    if(p>1):
        return 0
    if(mem[i][j][k]!=-1):
        return mem[i][j][k]
    ans = 0
    if(i==r):
        ans = dp(i,j+1,k+1)+G[j]*B[k]
        return ans
    elif(j==g):
        ans = dp(i+1,j,k+1)+R[i]*B[k]
    elif(k==b):
        ans = dp(i+1,j+1,k)+R[i]*G[j]
    else:
        ans = max(dp(i+1,j+1,k)+R[i]*G[j],dp(i,j+1,k+1)+G[j]*B[k],dp(i+1,j,k+1)+R[i]*B[k])
    mem[i][j][k] = ans
    return ans
print(dp(0,0,0))