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
    # n controls both number of patterns and edges
    # k is fixed to keep 2**k manageable but non-trivial
    k = 3
    # patterns
    patterns = []
    for i in range(n):
        # generate a k-length pattern using i in base-2 with '_' padding
        bits = []
        for j in range(k):
            if (i >> j) & 1:
                bits.append('a')
            else:
                bits.append('_')
        patterns.append(''.join(bits[:k]))
    # ensure uniqueness of patterns
    patterns = patterns[:n]
    n_actual = len(patterns)
    # map patterns to ids
    D = {s: i for i, s in enumerate(patterns)}

    def edges_from_pattern(s):
        Ans = set()
        for i in range(2 ** k):
            ans = [s[j] if (i >> j) & 1 else '_' for j in range(k)]
            Ans.add(''.join(ans))
        return Ans

    # build edges
    m = n  # one edge per node deterministically
    In = [set() for _ in range(n_actual)]
    Out = [set() for _ in range(n_actual)]
    flag = True

    for t in range(1, m + 1):
        # deterministically pick a string S from patterns
        S = patterns[(t - 1) % n_actual]
        for e in edges_from_pattern(S):
            if e in D and D[e] + 1:
                Out[t - 1].add(D[e])
                In[D[e]].add(t - 1)
        if (t - 1) not in Out[t - 1]:
            flag = False
            break
        else:
            if (t - 1) in Out[t - 1]:
                Out[t - 1].remove(t - 1)
            if (t - 1) in In[t - 1]:
                In[t - 1].remove(t - 1)

    return n_actual, m, k, patterns, D, In, Out, flag

def main(n):
    n_actual, m, k, patterns, D, In, Out, flag = generate_input(n)
    T = topological_sort(In, Out)
    if flag and T:
        print('YES')
        print(*[t + 1 for t in T])
    else:
        print('NO')

if __name__ == "__main__":
    main(10)