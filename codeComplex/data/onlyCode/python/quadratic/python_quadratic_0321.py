import sys
input = sys.stdin.buffer.readline

from collections import deque

n,d,k=map(int,input().split())

if d>=n:
    print("NO")
    exit()

graph=[[] for i in range(n+1)]

for i in range(1,d+2):
    graph[i].append(min(i-1,d+1-i))

# print(graph)

for i in range(1,d+1):
    graph[i].append(i+1)
    graph[i+1].append(i)
# print(graph)

deg=[0]*(n+1)
deg[1]=1
deg[d+1]=1
for i in range(2,d+1):
    deg[i]=2
# print(deg)
for i in deg:
    if i>k:
        print("NO")
        exit()

p=d+2
for i in range(1,d+2):
    q=deque()
    q.append(i)
    while len(q)!=0:
        x=q.popleft()
        while (graph[x][0]>0 and deg[x]<k and p<=n):
            graph[x].append(p)
            deg[x]=deg[x]+1
            graph[p].append(graph[x][0]-1)
            graph[p].append(x)
            deg[p]=deg[p]+1
            q.append(p)
            p=p+1
    # print(graph)        

if p<=n:
    print("NO")
else:
    print("YES")  
    vis=[-1]*(n+1)

    for i in range(1,d+2):
        if vis[i]==-1:
            q=deque()
            q.append(i)
            while len(q)!=0:
                x=q.popleft()
                vis[x]=1
                for j in range(1,len(graph[x])):
                    if vis[graph[x][j]]==-1:
                        print(x,graph[x][j])
                        q.append(graph[x][j])

