import sys
from collections import deque, defaultdict

def topological_sort(In, Out):
    dq, L = deque(), []
    for i, I in enumerate(In):
        if not I:
            dq.append(i)
    while dq:
        v = dq.popleft()
        L.append(v)
        for w in Out[v]:
            In[w].remove(v)
            if not In[w]:
                dq.append(w)
    if len(L) < len(In):
        return False
    return L

def generate_data(n):
    # Scale parameters with n
    k = max(1, min(5, n // 2))      # pattern length
    num_nodes = n                   # number of nodes n
    num_edges = max(1, n * 2)       # number of pattern edges m

    # Generate all patterns of length k over alphabet {'a', 'b'}
    # total 2**k patterns; we only use the first num_nodes of them
    patterns = []
    for x in range(1 << k):
        s = []
        for j in range(k):
            s.append('a' if (x >> j) & 1 else 'b')
        patterns.append(''.join(s))
    # Ensure we have enough patterns; if not, cycle
    P = [patterns[i % len(patterns)] for i in range(num_nodes)]

    # edges: list of (S, t)
    edges = []
    for i in range(num_edges):
        S = P[i % num_nodes]
        # simple deterministic target node index in [1, num_nodes]
        t = (i * 7 + 3) % num_nodes + 1
        edges.append((S, t))

    return num_nodes, num_edges, k, P, edges

def main(n):
    n_nodes, m_edges, k, patterns, edges_list = generate_data(n)

    def edges(s):
        Ans = set()
        for i in range(2**k):
            ans = [s[j] if i>>j&1 else '_' for j in range(k)]
            Ans.add(''.join(ans))
        return Ans

    D = defaultdict(lambda : -1)
    for i in range(n_nodes):
        D[patterns[i]] = i

    flag = 1
    In, Out = [set() for _ in range(n_nodes)], [set() for _ in range(n_nodes)]
    for S, t in edges_list:
        for e in edges(S):
            if D[e]+1:
                Out[t-1].add(D[e])
                In[D[e]].add(t-1)
        if t-1 not in Out[t-1]:
            flag = 0
            break
        else:
            Out[t-1].remove(t-1)
            In[t-1].remove(t-1)

    T = topological_sort(In, Out)
    if flag and T:
        print('YES')
        print(*[t+1 for t in T], sep = ' ')
    else:
        print('NO')

if __name__ == "__main__":
    main(10)