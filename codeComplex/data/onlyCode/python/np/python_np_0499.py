import sys

sys.setrecursionlimit(10**5)
int1 = lambda x: int(x)-1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.buffer.readline())
def MI(): return map(int, sys.stdin.buffer.readline().split())
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def BI(): return sys.stdin.buffer.readline().rstrip()
def SI(): return sys.stdin.buffer.readline().rstrip().decode()
inf = 10**16
md = 10**9+7
# md = 998244353

trie = [{}]

def push(s, val):
    now = 0
    for c in s:
        if c not in trie[now]:
            trie[now][c] = len(trie)
            trie.append({})
        now = trie[now][c]
    trie[now]["end"] = val

def match(s):
    res = []
    stack = [(0, 0)]
    while stack:
        u, i = stack.pop()
        if i == k:
            res.append(trie[u]["end"])
            continue
        if s[i] in trie[u]:
            stack.append((trie[u][s[i]], i+1))
        if "_" in trie[u]:
            stack.append((trie[u]["_"], i+1))
    return res

n, m, k = MI()
for i in range(n):
    push(SI(), i)
# print(trie)

to = [[] for _ in range(n)]
for _ in range(m):
    s, u = SI().split()
    u = int(u)-1
    vv = match(s)

    notmatch = True
    for v in vv:
        if u == v: notmatch = False
        else: to[u].append(v)
    if notmatch:
        print("NO")
        exit()

vis=[-1]*n
topo=[]
for u in range(n):
    if vis[u]==1:continue
    stack=[u]
    while stack:
        u=stack.pop()
        if vis[u]==-1:
            vis[u]=0
            stack.append(u)
            for v in to[u]:
                if vis[v]==0:
                    print("NO")
                    exit()
                if vis[v]==-1:
                    stack.append(v)
        elif vis[u]==0:
            topo.append(u+1)
            vis[u]=1

print("YES")
print(*topo[::-1])
