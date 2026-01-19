def main(n):
    from collections import defaultdict, deque

    k = 3
    m = n

    def edges(s):
        Ans = set()
        for i in range(2 ** k):
            ans = ''
            for j in range(k):
                if i >> j & 1:
                    ans = ans + s[j]
                else:
                    ans = ans + '_'
            Ans.add(ans)
        return Ans

    D = defaultdict(lambda: -1)
    base_chars = ['a', 'b', 'c']
    words = []
    for i in range(n):
        w = ''.join(base_chars[(i + j) % k] for j in range(k))
        words.append(w)
        D[w] = i

    flag = 1
    In = [set() for _ in range(n)]
    Out = [set() for _ in range(n)]

    for idx in range(m):
        S = words[idx % n]
        t = (idx % n) + 1
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

    def topological_sort(In, Out):
        dq = deque()
        L = []
        for i, I in enumerate(In):
            if not I:
                dq.append(i)
        while dq:
            v = dq.popleft()
            L.append(v)
            for w in Out[v]:
                if v in In[w]:
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