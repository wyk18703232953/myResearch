"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""
from itertools import product
import itertools
#from collections import defaultdict
import sys
import heapq
from collections import deque
MOD=1000000000007
#fin = open ('loan.in', 'r')
#fout = open ('loan.out', 'w')
#print(dic["4734"])
def find(parent,i):


    if parent[i] != i: 
        parent[i]=find(parent,parent[i]) 
    return parent[i] 

        # A utility function to do union of two subsets 
def union(parent,rank,xx,yy): 
    x=find(parent,xx)
    y=find(parent,yy)
    if rank[x]>rank[y]:
        parent[y]=x
    elif rank[y]>rank[x]:
        parent[x]=y
    else:
        parent[y]=x
        rank[x]+=1
ans=0
#NK=sys.stdin.readline().strip().split()
#K=int(sys.stdin.readline().strip())
#N=int(NK[0])
#K=int(NK[1])
#M=int(NK[2])
#ol=list(map(int,sys.stdin.readline().strip().split()))
#d={0:0,1:0}

x=0
y=0

MAX=1000000000
N,M,K=list(map(int,sys.stdin.readline().strip().split()))
W=[[[MAX,MAX,MAX,MAX] for j in range(M)] for i in range(N)] #L R U D
for i in range(N):
    l=list(map(int,sys.stdin.readline().strip().split()))
    for j in range(M-1):
        W[i][j][1]=l[j]
        W[i][j+1][0]=l[j]
for i in range(N-1):
    l=list(map(int,sys.stdin.readline().strip().split()))
    for j in range(M):
        #print(l,i,j)
        W[i][j][3]=l[j]
        W[i+1][j][2]=l[j]
        
#print(W)
if K%2==1:
    for i in range(N):
        ans=[]
        for j in range(M):
            ans.append("-1")
        print(" ".join(ans))
else:
    
    K=K//2
    dp=[[[0 for j in range(M)] for i in range(N)] for k in range(K+1)]
    for kt in range(1,K+1):
        
        dl=((0,-1),(0,1),(-1,0),(1,0))
        for i in range(N):
            for j in range(M):
                ans=MAX
                for t in range(4):
                    
                    ii,jj=dl[t]
                
                    if i+ii>=0 and i+ii<N and j+jj>=0 and j+jj<M:
                        ans=min(ans,dp[kt-1][i+ii][j+jj]+W[i][j][t]*2)
                    #print(i,j,ii,jj,ans)
                dp[kt][i][j]=ans
    #print(dp[-1])
    for i in range(N):
        ans=[]
        for j in range(M):
            ans.append(str(dp[-1][i][j]))
        print(" ".join(ans))

                
