n,m,k=list(map(int,input().split()))
p=[]
for _ in range(n):
    p.append(list(map(int,input().split())))
q=[]
for _ in range(n-1):
    q.append(list(map(int,input().split())))
def f(g):
    r=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            l=[]
            if i-1>=0:
                l.append(g[i-1][j]+q[i-1][j])
            if i+1<n:
                #print(i,j)
                l.append(g[i+1][j]+q[i][j])
            if j-1>=0:
                l.append(g[i][j-1]+p[i][j-1])
            if j+1<m:
                l.append(g[i][j+1]+p[i][j])
            r[i][j]=min(l)
    return r
g=[[0]*m for _ in range(n)]
if k%2!=0:
    for i in range(n):
        for j in range(m):
            g[i][j]=-1
        print(*g[i])
else:
    for _ in range(k//2):
       g=f(g)
    for i in range(n):
        for j in range(m):
            g[i][j]*=2
        print(*g[i])
        