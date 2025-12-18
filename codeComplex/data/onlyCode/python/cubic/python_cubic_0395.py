import sys, os

if os.environ['USERNAME']=='kissz':
    inp=open('in.txt','r').readline
    def debug(*args):
        print(*args,file=sys.stderr)
else:
    inp=sys.stdin.readline    
    def debug(*args):
        pass

# SCRIPT STARTS HERE

n,m,k=map(int,inp().split())
A=[[*map(int,inp().split())] for _ in range(n)]
B=[[*map(int,inp().split())] for _ in range(n-1)]
if k%2==0:
    O=[[[1e12]*m for _ in range(n)] for _ in range(k//2)]
    for i in range(n):
        for j in range(m):
            if i>0:
                O[0][i][j]=min(O[0][i][j],B[i-1][j])
            if i<n-1:
                O[0][i][j]=min(O[0][i][j],B[i][j])
            if j>0:
                O[0][i][j]=min(O[0][i][j],A[i][j-1])
            if j<m-1:
                O[0][i][j]=min(O[0][i][j],A[i][j])
    #for i in range(n):
    #    debug(*O[0][i])
    for l in range(1,k//2):
        for i in range(n):
            for j in range(m):
                if i>0:
                    O[l][i][j]=min(O[l][i][j],B[i-1][j]+O[l-1][i-1][j])
                if i<n-1:
                    O[l][i][j]=min(O[l][i][j],B[i][j]+O[l-1][i+1][j])
                if j>0:
                    O[l][i][j]=min(O[l][i][j],A[i][j-1]+O[l-1][i][j-1])
                if j<m-1:
                    O[l][i][j]=min(O[l][i][j],A[i][j]+O[l-1][i][j+1])         
                
        #for i in range(n):
        #    debug(*O[l][i])
    for i in range(n):
        print(*[O[-1][i][j]*2 for j in range(m)])
else:
    for i in range(n):
        print(*[-1]*m)
    

