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

def generate_deterministic_data(n):
    # Map n to N, M, K
    # N: number of strings/nodes
    # K: length of pattern strings
    # M: number of constraints
    if n < 3:
        n = 3
    K = 3
    N = n
    M = n

    # generate N distinct strings of length K over 'a'..'z'
    strings = []
    for i in range(N):
        s = []
        x = i
        for j in range(K):
            s.append(chr(ord('a') + (x % 26)))
            x //= 26
        strings.append(''.join(s))
    # dictionary mapping string to index
    dic = defaultdict(lambda: -1)
    for i, s in enumerate(strings):
        dic[s] = i

    # generate M constraints (t, mt)
    # t is one of the strings, mt is its index + 1 (1-based)
    constraints = []
    for i in range(M):
        idx = i % N
        t = strings[idx]
        mt = idx + 1
        constraints.append((t, mt))

    return N, M, K, dic, constraints

def core_algorithm(N, M, K, dic, constraints):
    G = Graph(N)
    for t, mt in constraints:
        mt = mt - 1
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
        if mt not in lis:
            return "NO", []
        for l in lis:
            if l != mt:
                G.add_edge(mt, l, bi=False, rev=False)
    G.topo_sort()
    if len(G.order) == N:
        return "YES", G.order
    else:
        return "NO", []

def main(n):
    N, M, K, dic, constraints = generate_deterministic_data(n)
    res, order = core_algorithm(N, M, K, dic, constraints)
    if res == "YES":
        print("YES")
        print(*order)
    else:
        print("NO")

if __name__ == "__main__":
    main(10)