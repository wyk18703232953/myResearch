import sys
input = sys.stdin.readline
from collections import deque
class Graph:
  def __init__(self, N, M=-1):
    self.V = N
    if M>=0: self.E = M
    self.edge = [[] for _ in range(self.V)]
    self.edge_rev = [[] for _ in range(self.V)]
    self.order = []
    self.to = [0]*self.V
    self.visited = [False]*self.V
    self.dp = [0]*self.V

  def add_edge(self, a, b, dist=-1, bi=False, rev=False):
    if dist>=0:
      self.edge[a].append((dist, b))
      if rev: self.edge_rev[b].append((dist, a))
      if bi: self.edge[b].append((dist, a))
    else:
      self.edge[a].append(b)
      self.to[b] += 1
      if rev: self.edge_rev[b].append(a)
      if bi: self.edge[b].append(a)

  def topo_sort(self): #topological sort
    updated = [0]*self.V
    for start in range(self.V):
      if self.to[start] or updated[start]: continue
      stack = deque([start])
      while stack:
        v = stack.popleft()
        self.order.append(v+1)
        updated[v] = 1
        for u in self.edge[v]:
          self.to[u] -= 1
          if self.to[u]: continue
          stack.append(u)

N, M, K = map(int, input().split())

from collections import defaultdict
dic = defaultdict(lambda: -1)
for i in range(N):
  S = input()[:-1]
  dic[S] = i
G = Graph(N)
for _ in range(M):
  t, mt = input().split()
  mt = int(mt)-1
  lis = []
  for S in range(1<<K):
    s = ''
    for i in range(K):
      if (S>>i)%2:
        s += '_'
      else:
        s += t[i]
    if dic[s]>=0: lis.append(dic[s])
  if mt not in lis:
    print('NO')
    exit()
  for l in lis:
    if l!=mt:
      G.add_edge(mt, l, bi=False, rev=False)
G.topo_sort()
if len(G.order)==N:
  print('YES')
  print(*G.order)
else:
  print('NO')