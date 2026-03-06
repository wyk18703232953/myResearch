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

def generate_string_patterns(k):
    # generate 2^k strings over 'a' and 'b'
    res = []
    for i in range(1 << k):
        s = []
        for j in range(k):
            if (i >> j) & 1:
                s.append('a')
            else:
                s.append('b')
        res.append(''.join(s))
    return res

def main(n):
    # map n to parameters:
    # k: length of strings (small, controls 2^k)
    # n_var: number of strings
    # m: number of constraints
    if n <= 0:
        return

    # choose k so that 2^k <= max(4, n)
    k = 1
    while (1 << k) <= max(4, n) and k < 12:
        k += 1
    k = max(1, k - 1)

    # number of variables
    n_var = max(1, n)
    # number of constraints
    m = max(1, 2 * n)

    # generate base string patterns of length k
    base_patterns = generate_string_patterns(k)
    num_patterns = len(base_patterns)

    # deterministically construct n_var strings by cycling base patterns
    strings = [base_patterns[i % num_patterns] for i in range(n_var)]

    # build D: mapping from all possible edges(s) strings to index or -1
    # here we map only generated strings; other patterns remain -1
    from collections import defaultdict
    D = defaultdict(lambda: -1)
    for i, s in enumerate(strings):
        D[s] = i

    def edges(s):
        Ans = set()
        for i in range(1 << k):
            ans = ''
            for j in range(k):
                if (i >> j) & 1:
                    ans = ''.join([ans, s[j]])
                else:
                    ans = ''.join([ans, '_'])
            Ans.add(ans)
        return Ans

    In = [set() for _ in range(n_var)]
    Out = [set() for _ in range(n_var)]

    flag = 1

    # generate m constraints deterministically
    for idx in range(m):
        # choose S as one of existing strings
        s_idx = idx % n_var
        S = strings[s_idx]
        # choose t as 1..n_var in a cycle
        t = (idx % n_var) + 1

        for e in edges(S):
            if D[e] + 1:
                Out[t - 1].add(D[e])
                In[D[e]].add(t - 1)
        # enforce self-loop as in original logic
        Out[t - 1].add(t - 1)
        In[t - 1].add(t - 1)

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