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

    # Deterministically define parameters based on n
    if n < 1:
        n = 1
    k = max(1, n % 6 + 1)      # pattern length between 1 and 6
    m = max(1, 2 * n)          # number of queries

    # Generate all k-length patterns over 'a' and '_'
    patterns = []
    base = ['a', '_']
    def gen_pattern(idx, cur):
        if idx == k:
            patterns.append(''.join(cur))
            return
        for ch in base:
            cur.append(ch)
            gen_pattern(idx + 1, cur)
            cur.pop()
    gen_pattern(0, [])
    total_patterns = len(patterns)
    if n > total_patterns:
        n = total_patterns

    # D: pattern -> index, use first n patterns
    D = defaultdict(lambda: -1)
    for i in range(n):
        D[patterns[i]] = i

    def edges(s):
        Ans = set()
        # generate all masks by replacing positions with '_'
        for i in range(1 << k):
            ans = [s[j] if (i >> j) & 1 else '_' for j in range(k)]
            Ans.add(''.join(ans))
        return Ans

    flag = True
    In = [set() for _ in range(n)]
    Out = [set() for _ in range(n)]

    # Deterministic generation of m queries (S, t)
    # S is chosen cyclically from first n patterns
    # t is in [1, n] deterministically
    for q in range(m):
        S = patterns[q % n]
        t = (q % n) + 1  # 1-based

        for e in edges(S):
            if D[e] + 1:
                Out[t - 1].add(D[e])
                In[D[e]].add(t - 1)
        if t - 1 not in Out[t - 1]:
            flag = False
            break
        else:
            Out[t - 1].remove(t - 1)
            In[t - 1].remove(t - 1)

    T = topological_sort(In, Out)
    if flag and T:
        print('YES')
        print(*[t + 1 for t in T])
    else:
        print('NO')

if __name__ == "__main__":
    main(5)