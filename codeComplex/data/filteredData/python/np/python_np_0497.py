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

def generate_data(n):
    if n < 1:
        n = 1
    k = max(1, n.bit_length() // 2)
    m = n
    strings = []
    for i in range(n):
        s = []
        x = i
        for j in range(k):
            s.append(chr(ord('a') + (x % 3)))
            x //= 3
        strings.append(''.join(s))
    queries = []
    for i in range(m):
        S = strings[i % n]
        t = (i * 7 + 3) % n + 1
        queries.append((S, t))
    return n, m, k, strings, queries

def main(n):
    from collections import defaultdict
    n, m, k, strings, queries = generate_data(n)

    def edges(s):
        Ans = set()
        for i in range(2 ** k):
            ans = [s[j] if (i >> j) & 1 else '_' for j in range(k)]
            Ans.add(''.join(ans))
        return Ans

    D = defaultdict(lambda: -1)
    for i in range(n):
        D[strings[i]] = i

    flag = 1
    In = [set() for _ in range(n)]
    Out = [set() for _ in range(n)]
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
    if flag and T:
        print('YES')
        print(*[t + 1 for t in T], sep=' ')
    else:
        print('NO')

if __name__ == "__main__":
    main(10)