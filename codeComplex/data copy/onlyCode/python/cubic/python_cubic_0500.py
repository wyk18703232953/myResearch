import sys,math
class Node:
    def __init__(self,u=math.inf,d=math.inf,l=math.inf,r=math.inf):
        self.up=u
        self.dn=d
        self.lt=l
        self.rt=r
    def __str__(self):
        return 'U:{},D:{},L:{},R:{}'.format(self.up,self.dn,self.lt,self.rt)

n,m,k=list(map(int,sys.stdin.readline().strip().split()))
graph=[[Node() for j in range(m)]for i in range(n)]
for i in range(n):
    wts=list(map(int,sys.stdin.readline().strip().split()))
    for j in range(m-1):
        graph[i][j].rt=wts[j]
        graph[i][j+1].lt=wts[j]

for i in range(n-1):
    wts=list(map(int,sys.stdin.readline().strip().split()))
    for j in range(m):
        graph[i][j].dn=wts[j]
        graph[i+1][j].up=wts[j]

ans=[[math.inf for j in range(m)]for i in range(n)]

if k%2:
    [[print(' '.join(list(map(lambda x:str(-1) if x==math.inf else str(x),s))))]for s in ans]
    
else:
    def bfs(prsnt,stps):
        # print(prsnt,stps)
        if stps==0:
            return 0
        else:
            if dp[prsnt[0]][prsnt[1]][stps]==math.inf:
                min_cost=math.inf
                for x,y,c in [(0,1,graph[prsnt[0]][prsnt[1]].dn),(1,0,graph[prsnt[0]][prsnt[1]].rt),(0,-1,graph[prsnt[0]][prsnt[1]].up),(-1,0,graph[prsnt[0]][prsnt[1]].lt)]:
                    if -1<prsnt[1]+x<m and -1<prsnt[0]+y<n:
                        min_cost=min(bfs((prsnt[0]+y,prsnt[1]+x),stps-1)+c,min_cost)
                dp[prsnt[0]][prsnt[1]][stps]=min_cost
                return min_cost
            else:
                return dp[prsnt[0]][prsnt[1]][stps]

    dp=[[[math.inf for k in range(k+1)] for j in range(m)]for i in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j]=bfs((i,j),k//2)*2
    [[print(' '.join(list(map(lambda x:str(-1) if x==math.inf else str(x),s))))]for s in ans]