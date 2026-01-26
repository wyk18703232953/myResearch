import sys
# sys.setrecursionlimit(10**6) 
input=sys.stdin.readline
def  f(r,g,b,n,m,k):
    # s=str(n)+"_"+str(m)+"_"+str(k)
    # print(n,m,k)
    if((n>=1 and m>=1) or (k>=1 and m>=1) or(n>=1 and k>=1)):
        # print(n,m,k,"zzz")
        a1=mat[n][m][k]
        if(a1!=-1):
            return a1
        else:
            a1=0
            b1=0
            c1=0
            # print(n,m,k)
            if(n>=1 and m>=1):
          
                a1=r[n-1]*g[m-1] + f(r,g,b,n-1,m-1,k)
            if(k>=1 and m>=1):
                b1=b[k-1]*g[m-1] + f(r,g,b,n,m-1,k-1)
            if(n>=1 and k>=1):
                c1=r[n-1]*b[k-1] + f(r,g,b,n-1,m,k-1)
            # if(n>=0 and m>=0 and k>=0):
            mat[n][m][k]=max(a1,b1)
            mat[n][m][k]=max(mat[n][m][k],c1)
            # print(d[s])
            return mat[n][m][k]
    return 0


n,m,k=list(map(int,input().split(" ")))
mat=[[[-1 for i in range(k+1)] for j in range(m+1)]for z in range(n+1)]
# print(mat)
r=list(map(int,input().split(" ")))
g=list(map(int,input().split(" ")))
b=list(map(int,input().split(" ")))
r.sort()
g.sort()
b.sort()
# print(r,g,b)
d={}
print(f(r,g,b,n,m,k))