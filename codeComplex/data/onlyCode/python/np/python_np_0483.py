import sys
from enum import Enum

class flag(Enum):
    UNVISITED = -1
    EXPLORED = -2
    VISITED = -3

def match(p, s):
    for i in range(len(p)):
        if p[i] != "_" and p[i] != s[i]:
            return False
    return True

def cycleCheck(u):
    global AL
    global dfs_num
    global dfs_parent
    global sol

    dfs_num[u] = flag.EXPLORED.value
    for v in AL[u]:
        if dfs_num[v] == flag.UNVISITED.value:
            dfs_parent[v] = u
            cycleCheck(v)
        elif dfs_num[v] == flag.EXPLORED.value:
            sol = False
    dfs_num[u] = flag.VISITED.value

def toposort(u):
    global AL
    global dfs_num
    global ts

    dfs_num[u] = flag.VISITED.value
    for v in AL[u]:
        if dfs_num[v] == flag.UNVISITED.value:
            toposort(v)
    ts.append(u)

sol = True
n, m, k = map(int, sys.stdin.readline().strip().split())
pd = {}
ps = set()
pa = []
for i in range(n):
    p = sys.stdin.readline().strip()
    pd[p] = i + 1
    ps.add(p)
    pa.append(p)

AL = [[] for _ in range(n)]

for _ in range(m):
    s, fn = sys.stdin.readline().strip().split()
    fn = int(fn)
    if not match(pa[fn-1], s):
        sol = False
        
    mm = [""]
    for i in s:
        mm = list(map(lambda x: x + "_", mm)) + list(map(lambda x: x + i, mm))
    for i in mm:
        if i in ps:
            if pd[i] != fn:
                AL[fn-1].append(pd[i]-1)

try:    
    if not sol:
        print("NO")
    else:
        dfs_num = [flag.UNVISITED.value] * n
        dfs_parent = [-1] * n
        for u in range(n):
            if dfs_num[u] == flag.UNVISITED.value:
                cycleCheck(u)
        if not sol:
            print("NO")
        else:
            dfs_num = [flag.UNVISITED.value] * n
            ts = []
            for u in range(n):
                if dfs_num[u] == flag.UNVISITED.value:
                    toposort(u)
            ts = ts[::-1]
            print("YES")
            print(' '.join(map(lambda x: str(x+1), ts)))
except:
    print("NO")