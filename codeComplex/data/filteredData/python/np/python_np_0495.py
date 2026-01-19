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

def generate_input(n):
    # Deterministic mapping from n to (n_nodes, m_edges, k_len, patterns, queries)
    if n <= 0:
        n_nodes = 1
    else:
        n_nodes = n
    k_len = 3 if n_nodes >= 3 else max(1, n_nodes)
    m_edges = n_nodes * 2

    # Generate patterns (strings of length k_len)
    patterns = []
    for i in range(n_nodes):
        s = []
        for j in range(k_len):
            s.append(chr(ord('a') + (i + j) % 3))
        patterns.append(''.join(s))

    # Map index to pattern directly
    # Generate m_edges queries (S, t)
    queries = []
    for i in range(m_edges):
        t = (i % n_nodes) + 1
        S = patterns[i % n_nodes]
        queries.append((S, t))

    return n_nodes, m_edges, k_len, patterns, queries

def main(n):
    n_nodes, m, k, patterns, queries = generate_input(n)

    def edges(s):
        Ans = set()
        for i in range(2 ** k):
            ans = ''
            for j in range(k):
                if i >> j & 1:
                    ans = ''.join([ans, s[j]])
                else:
                    ans = ''.join([ans, '_'])
            Ans.add(ans)
        return Ans

    D = defaultdict(lambda: -1)
    for i in range(n_nodes):
        D[patterns[i]] = i

    flag = 1
    In, Out = [set() for _ in range(n_nodes)], [set() for _ in range(n_nodes)]
    for S, t in queries:
        for e in edges(S):
            if D[e] + 1:
                Out[t - 1].add(D[e])
                In[D[e]].add(t - 1)
        if t - 1 not in Out[t - 1]:
            flag = 0
            break
        else:
            Out[t - 1].remove(t - 1)
            In[t - 1].remove(t - 1)

    T = topological_sort(In, Out)
    if flag == 0 or not T:
        print('NO')
    else:
        print('YES')
        print(*[t + 1 for t in T], sep=' ')

if __name__ == "__main__":
    main(5)