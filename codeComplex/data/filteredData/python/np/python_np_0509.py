import sys
from collections import deque, defaultdict

class Graph:
    def __init__(self, N, M=-1):
        self.V = N
        if M >= 0:
            self.E = M
        self.edge = [[] for _ in range(self.V)]
        self.edge_rev = [[] for _ in range(self.V)]
        self.order = []
        self.to = [0] * self.V
        self.visited = [False] * self.V
        self.dp = [0] * self.V

    def add_edge(self, a, b, dist=-1, bi=False, rev=False):
        if dist >= 0:
            self.edge[a].append((dist, b))
            if rev:
                self.edge_rev[b].append((dist, a))
            if bi:
                self.edge[b].append((dist, a))
        else:
            self.edge[a].append(b)
            self.to[b] += 1
            if rev:
                self.edge_rev[b].append(a)
            if bi:
                self.edge[b].append(a)

    def topo_sort(self):
        updated = [0] * self.V
        for start in range(self.V):
            if self.to[start] or updated[start]:
                continue
            stack = deque([start])
            while stack:
                v = stack.popleft()
                self.order.append(v + 1)
                updated[v] = 1
                for u in self.edge[v]:
                    self.to[u] -= 1
                    if self.to[u]:
                        continue
                    stack.append(u)

def deterministic_data(n):
    # Interpret n as number of patterns N
    # Choose fixed K=3
    K = 3
    if n < 1:
        n = 1
    N = n
    # Generate N distinct strings of length K over 'a','b'
    S_list = []
    for i in range(N):
        chars = []
        for j in range(K):
            bit = (i >> j) & 1
            chars.append('a' if bit == 0 else 'b')
        s = ''.join(chars[:K])
        S_list.append(s)
    # Generate M edges; let M = min(N*2, N*(2**K))
    max_patterns = 1 << K
    M = min(N * 2, N * max_patterns) if N > 0 else 0
    edges = []
    for e in range(M):
        t_index = e % N
        t = S_list[t_index]
        mt = (t_index + 1) % N  # 1-based in original, will convert to 0-based later
        edges.append((t, mt))
    return N, M, K, S_list, edges

def run_algorithm(N, M, K, S_list, edges):
    dic = defaultdict(lambda: -1)
    for i in range(N):
        S = S_list[i]
        dic[S] = i
    G = Graph(N)
    for t, mt in edges:
        mt_idx = mt - 1
        lis = []
        for S in range(1 << K):
            s = ''
            for i in range(K):
                if (S >> i) % 2:
                    s += '_'
                else:
                    s += t[i]
            if dic[s] >= 0:
                lis.append(dic[s])
        if mt_idx not in lis:
            return "NO", []
        for l in lis:
            if l != mt_idx:
                G.add_edge(mt_idx, l, bi=False, rev=False)
    G.topo_sort()
    if len(G.order) == N:
        return "YES", G.order
    else:
        return "NO", []

def main(n):
    N, M, K, S_list, edges = deterministic_data(n)
    result, order = run_algorithm(N, M, K, S_list, edges)
    if result == "YES":
        print("YES")
        print(*order)
    else:
        print("NO")

if __name__ == "__main__":
    main(5)