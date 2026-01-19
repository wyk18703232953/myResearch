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

def make_edges_func(k):
    def edges(s):
        Ans = set()
        for i in range(2 ** k):
            ans = [s[j] if (i >> j) & 1 else '_' for j in range(k)]
            Ans.add(''.join(ans))
        return Ans
    return edges

def generate_data(n):
    # Interpret n as number of nodes; build a fixed pattern of m and k
    if n < 1:
        n = 1
    k = 3
    # m grows linearly with n to scale the graph size
    m = max(1, 3 * n)

    # Generate all possible patterns of length k over {'a','b','_'}
    chars = ['a', 'b', '_']
    patterns = []
    for i in range(len(chars) ** k):
        s = []
        x = i
        for _ in range(k):
            s.append(chars[x % len(chars)])
            x //= len(chars)
        patterns.append(''.join(s))
    # Use first n patterns as the base strings for vertices
    base_strings = [patterns[i % len(patterns)] for i in range(n)]

    # Build mapping D: string -> index (similar to original input phase)
    D = defaultdict(lambda: -1)
    for i, s in enumerate(base_strings):
        D[s] = i

    edges_list = []
    edges = make_edges_func(k)

    # For each vertex t, create an edge description (S, t)
    # S is chosen deterministically from patterns based on t and an offset
    for t in range(1, n + 1):
        base_idx = (t * 7) % len(patterns)
        S = patterns[base_idx]
        edges_list.append((S, t))

    # If we need more than n edges, add more with different offsets
    offset = 1
    while len(edges_list) < m:
        for t in range(1, n + 1):
            if len(edges_list) >= m:
                break
            base_idx = (t * 7 + offset * 5) % len(patterns)
            S = patterns[base_idx]
            edges_list.append((S, t))
        offset += 1

    return n, m, k, D, edges_list, edges

def main(n):
    n, m, k, D, edges_list, edges = generate_data(n)

    flag = 1
    In = [set() for _ in range(n)]
    Out = [set() for _ in range(n)]

    processed = 0
    for S, t in edges_list:
        processed += 1

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
    main(10)