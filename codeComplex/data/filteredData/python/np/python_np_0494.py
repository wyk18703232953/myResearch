def main(n):
    from collections import defaultdict, deque

    # Map n to problem parameters
    # Choose k small (bitmask dimension), m proportional to n, and n as number of strings
    if n < 1:
        return
    k = 3
    num_vertices = n
    num_edges = max(1, n * 2)
    D = defaultdict(lambda: -1)

    # Generate base strings of length k over characters 'a'.. with '_' allowed
    # Ensure they form a deterministic set
    base_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    strings = []
    for i in range(num_vertices):
        s = []
        for j in range(k):
            # deterministic pattern based on i and j
            idx = (i + j) % len(base_chars)
            s.append(base_chars[idx])
        strings.append(''.join(s))

    # edges function from original code
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

    # Build dictionary D mapping masks to indices
    for i in range(num_vertices):
        D[strings[i]] = i
        # also add some masked versions to D to make edges meaningful
        for e in edges(strings[i]):
            if D[e] == -1:
                D[e] = i

    flag = 1
    In = [set() for _ in range(num_vertices)]
    Out = [set() for _ in range(num_vertices)]

    # Generate deterministic edges (S, t)
    # S will be one of the base strings, t is a vertex index (1-based)
    # Try to create self-loop for some, and other edges based on pattern
    for e_idx in range(num_edges):
        t = (e_idx % num_vertices) + 1
        s_idx = (e_idx * 2) % num_vertices
        S = strings[s_idx]

        for e in edges(S):
            if D[e] + 1:
                Out[t - 1].add(D[e])
                In[D[e]].add(t - 1)
        # enforce original self-loop constraint
        if t - 1 not in Out[t - 1]:
            flag = 0
            break
        else:
            Out[t - 1].remove(t - 1)
            In[t - 1].remove(t - 1)

    def topological_sort(In, Out):
        dq = deque()
        L = []
        for i, I in enumerate(In):
            if not I:
                dq.append(i)
        while dq:
            v = dq.popleft()
            L.append(v)
            for w in list(Out[v]):
                In[w].remove(v)
                if not In[w]:
                    dq.append(w)
        if len(L) < len(In):
            return False
        return L

    T = topological_sort(In, Out)
    if flag == 0 or not T:
        print('NO')
    else:
        print('YES')
        print(*[t + 1 for t in T], sep=' ')


if __name__ == "__main__":
    main(10)