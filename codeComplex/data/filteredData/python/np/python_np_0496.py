def topological_sort(In, Out):
    from collections import deque
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

def main(n):
    from collections import defaultdict

    # Define scale parameters based on n
    # n_nodes = n
    # k = max(1, n.bit_length() // 2)   # pattern length
    # m = n * 2                         # number of constraints
    n_nodes = max(1, n)
    k = max(1, n.bit_length() // 2)
    m = n_nodes * 2

    # Deterministically generate strings of length k over alphabet {'a','b','c'}
    alphabet = ['a', 'b', 'c']

    def gen_string(idx):
        s = []
        base = len(alphabet)
        x = idx
        for _ in range(k):
            s.append(alphabet[x % base])
            x //= base
        return ''.join(s)

    # Build dictionary D: pattern -> index
    D = defaultdict(lambda: -1)
    limit = min(n_nodes, 3 ** min(k, 10))
    for i in range(limit):
        D[gen_string(i)] = i
    # For remaining indices (if any), map deterministic underscore-based strings
    for i in range(limit, n_nodes):
        s = ''.join('_' if (i >> j) & 1 else alphabet[(i + j) % 3] for j in range(k))
        D[s] = i

    def edges(s):
        Ans = set()
        for i in range(2 ** k):
            ans = [s[j] if (i >> j) & 1 else '_' for j in range(k)]
            Ans.add(''.join(ans))
        return Ans

    flag = 1
    In = [set() for _ in range(n_nodes)]
    Out = [set() for _ in range(n_nodes)]

    # Deterministically generate m constraints (S, t)
    for idx in range(m):
        S = gen_string((idx * 7 + 3) % max(1, limit))
        t = (idx * 5 + 1) % n_nodes + 1

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