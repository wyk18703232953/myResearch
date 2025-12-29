# Converted version: no input(), with main(n) generating test data.

from collections import deque, defaultdict
import random
import string

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

def main(n):
    # -----------------------------
    # 1. Generate parameters
    # -----------------------------
    # k: pattern length
    k = max(1, min(4, n))  # keep k small so 2**k is manageable

    # All patterns over alphabet {'a','b'} with length k
    def all_patterns(k):
        res = []
        for mask in range(1 << k):
            s = []
            for j in range(k):
                s.append('a' if (mask >> j) & 1 else 'b')
            res.append(''.join(s))
        return res

    patterns = all_patterns(k)
    total_patterns = len(patterns)

    # We will use first n of them as base strings (or repeat if n > total_patterns)
    base_strings = [patterns[i % total_patterns] for i in range(n)]

    # Build D: mapping string -> index
    D = defaultdict(lambda: -1)
    for i, s in enumerate(base_strings):
        D[s] = i

    # -----------------------------
    # 2. Generate edges
    # -----------------------------
    # We will attempt to generate m constraints (S, t)
    # and try to keep the graph acyclic most of the time.
    # For simplicity, set m proportional to n.
    m = max(1, 2 * n)

    # edges(S) as in original code
    def edges(s):
        Ans = set()
        for i in range(1 << k):
            ans = [s[j] if (i >> j) & 1 else '_' for j in range(k)]
            Ans.add(''.join(ans))
        return Ans

    In = [set() for _ in range(n)]
    Out = [set() for _ in range(n)]
    flag = 1

    # To ensure a valid self-loop t-1 in Out[t-1], we'll insert it first, then remove it as original does.
    # For generating S: sometimes equal to base_strings[t-1], sometimes random from patterns.
    for _ in range(m):
        t = random.randint(1, n)

        # generate S
        if random.random() < 0.5:
            S = base_strings[t - 1]
        else:
            S = random.choice(patterns)

        # Put a self-loop first, so that condition `t-1 in Out[t-1]` holds, then we remove it.
        Out[t - 1].add(t - 1)
        In[t - 1].add(t - 1)

        for e in edges(S):
            if D[e] + 1:
                Out[t - 1].add(D[e])
                In[D[e]].add(t - 1)

        # original code checks and then removes self-loop
        if (t - 1) not in Out[t - 1]:
            flag = 0
            break
        else:
            Out[t - 1].remove(t - 1)
            In[t - 1].remove(t - 1)

    # -----------------------------
    # 3. Run logic and print result
    # -----------------------------
    T = topological_sort([s.copy() for s in In], [s.copy() for s in Out])

    if flag == 0 or not T:
        print('NO')
    else:
        print('YES')
        print(*[t + 1 for t in T], sep=' ')


if __name__ == "__main__":
    # example run
    main(5)