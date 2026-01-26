from sys import stdin, stdout 
input = stdin.readline
 
n,m,K = map(int,input().split())
edges = []
for i in range(n):
    edges.append([[]])
    lis = list(map(int,input().split()))
    for j in range(m-1):
        edges[i][j].append((1,0,lis[j]))
        edges[i].append([])
        edges[i][j+1].append((-1,0,lis[j]))
for i in range(n-1):
    lis = list(map(int,input().split()))
    for j in range(m):
        edges[i][j].append((0,1,lis[j]))
        edges[i+1][j].append((0,-1,lis[j]))

if K%2==1:
    lis = []
    for i in range(n):
        lis.append([-1]*m)
else:
    lis = []
    for i in range(n):
        lis.append([0]*m)
        
    for k in range(1,(K//2)+1):
        new_lis = []
        for i in range(n):
            new_lis.append([0]*m)
        for i in range(n):
            for j in range(m):
                dist = []
                for e in edges[i][j]:
                    # print(e,i,j,lis)
                    dist.append(e[2] + lis[i+e[1]][j+e[0]])
                new_lis[i][j] = min(dist)
        lis = new_lis
    for i in range(n):
        for j in range(m):
            lis[i][j] *= 2
            
for i in lis:
    print(*i)