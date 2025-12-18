import collections,sys,functools,heapq,bisect,math

def binary(s):
    ans = set()
    for i in range(2**len(s)):
        x = []
        for j in range(len(s)):
            if (i>>j) & 1:
                x.append(s[j])
            else:
                x.append('_')
        ans.add(''.join(x))
    return ans   

seen = set()
visited = set()
ans = []
def dfs(i):
    visited.add(i)
    seen.add(i)
    for j in graph[i]:
        if j in visited:
            return True
        if j in seen:
            continue
        if dfs(j):
            return True
    ans.append(str(i))
    visited.remove(i)
    return False 

def topo(graph):
    seen.clear()
    for i in range(1,n+1):
        if i in seen:
            continue
        if dfs(i):
            return False
    return True    
    
input = sys.stdin.readline
mod = 10**9 + 7

#t = int(input())
for _ in range(1):
    n,m,k = map(int,input().strip().split())
    d = {}
    dop = {}
    for i in range(1,n+1):
        d[i] = input().strip()
        dop[d[i]] = i 
        
        
    graph = collections.defaultdict(list)
    for i in range(m):
        s = input().strip().split()
        ind = int(s[1])
        sset = binary(s[0])
        #print(s,sset)
        if d[ind] not in sset:
            print('NO')
            break
        for i in sset:
            if i in dop and dop[i] != ind :
                graph[dop[i]].append(ind)
    else:
        #print(graph)
        if topo(graph):
            print('YES')
            print(' '.join(ans))
        else:
            print('NO')
            
    