# import io.os
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def func(n1,n2,n3):
    global r,g,b 
    if((n1<0 and n2<0) or (n3<0 and n2<0) or (n1<0 and n3<0) ):
        return 0 
    if(n1<0):
        return g[n2]*b[n3] + func(n1,n2-1,n3-1)
    if(n2<0):
        return r[n1]*b[n3] + func(n1-1,n2,n3-1)
    if(n3<0):
        return g[n2]*r[n1] + func(n1-1,n2-1,n3)
    if(dp[n1][n2][n3]==-1):
        dp[n1][n2][n3]= max(g[n2]*b[n3] + func(n1,n2-1,n3-1),r[n1]*b[n3] + func(n1-1,n2,n3-1),g[n2]*r[n1] + func(n1-1,n2-1,n3))
    return dp[n1][n2][n3]

# def func(n1,n2,n3):
#     for i in range(n1):
#         for j in range(n2):
#             for k in range(n3):
#                 if(i==0 and j==0 and k==0):
#                     dp[i][j][k] = max(r[i]*g[j],g[j]*b[k],b[k]*r[i])
#                 elif(i==0 and j==0):
#                     dp[i][j][k]=max(g[j]*b[k] + dp[i][j-1][k-1],r[i]*b[k] + dp[i-1][j][k-1],g[j]*r[i] + dp[i-1][j-1][k])
#                 dp[i][j][k]=max(g[j]*b[k] + dp[i][j-1][k-1],r[i]*b[k] + dp[i-1][j][k-1],g[j]*r[i] + dp[i-1][j-1][k])

R,G,B=tuple(map(int,input().split()))
r=list(map(int,input().split()))
g=list(map(int,input().split()))
b=list(map(int,input().split()))
r=sorted(r)
g=sorted(g)
b=sorted(b)
prefix1=[0]*R 
prefix2 = [0]*G 
prefix3 = [0]*B 
prefix1[0]=r[0]
prefix2[0] = g[0]
prefix3[0]=b[0]
dp=[[[-1 for i in range(B)] for j in range(G)]for k in range(R)]
# for i in range(1,R):
#     prefix1[i]=prefix1[i-1]*r[i]
# for i in range(1,G):
#     prefix2[i]=prefix2[i-1]*g[i]
# for i in range(1,B):
#     prefix3[i]=prefix3[i-1]*b[i]
print(func(R-1,G-1,B-1))