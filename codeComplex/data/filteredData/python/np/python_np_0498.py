# Converted from original CF-E-00 style code
# - Removed all input()
# - Added main(n) with synthetic test generation based on size parameter n
# - Logic preserved

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
        for w in list(Out[v]):
            if v in In[w]:
                In[w].remove(v)
            if not In[w]:
                dq.append(w)
    if len(L) < len(In):
        return False
    return L


def main(n):
    """
    n: number of nodes / strings.
    Synthetic data generation strategy:
    - Fix k = 3 (pattern length) for simplicity.
    - Create n distinct strings of length k over 'a'..'c'.
    - Create m edges (patterns), each pattern is a string with '_' wildcard.
    """

    # 1. Parameters for data generation
    k = 3                      # length of base strings / patterns
    m = max(1, 2 * n)          # number of pattern edges
    alphabet = "abc"

    # 2. Generate n distinct strings of length k
    #    (if n exceeds alphabet^k, we cap n)
    max_strings = len(alphabet) ** k
    actual_n = min(n, max_strings)

    def index_to_string(idx):
        s = []
        base = len(alphabet)
        for _ in range(k):
            s.append(alphabet[idx % base])
            idx //= base
        return "".join(s)

    strings = [index_to_string(i) for i in range(actual_n)]

    # mapping: string -> index
    D = defaultdict(lambda: -1)
    for i, s in enumerate(strings):
        D[s] = i

    # 3. Define edges(s): all variants of s with '_' wildcard
    def edges(s):
        Ans = set()
        for mask in range(1 << k):
            tmp = [s[j] if (mask >> j) & 1 else '_' for j in range(k)]
            Ans.add(''.join(tmp))
        return Ans

    # 4. Generate m test patterns and target indices
    # We'll generate patterns that are guaranteed to exist in D sometimes,
    # and some random patterns that may or may not exist.
    patterns = []
    for _ in range(m):
        t = random.randrange(actual_n) + 1  # target index in [1, actual_n]
        base = strings[t - 1]

        # choose one of:
        #  - pattern derived from base
        #  - random pattern
        if random.random() < 0.7:
            # derive pattern from base: randomly set '_' at some positions
            pat = list(base)
            for j in range(k):
                if random.random() < 0.5:
                    pat[j] = '_'
            S = ''.join(pat)
        else:
            # random pattern: letters / '_'
            S = ''.join(
                random.choice(alphabet + '_')
                for _ in range(k)
            )
        patterns.append((S, t))

    # 5. Original logic using synthetic data
    flag = True
    In = [set() for _ in range(actual_n)]
    Out = [set() for _ in range(actual_n)]

    for S, t in patterns:
        t_idx = t - 1
        for e in edges(S):
            if D[e] + 1:
                Out[t_idx].add(D[e])
                In[D[e]].add(t_idx)

        # original self-loop check
        if t_idx not in Out[t_idx]:
            flag = False
            break
        else:
            Out[t_idx].remove(t_idx)
            if t_idx in In[t_idx]:
                In[t_idx].remove(t_idx)

    T = topological_sort(In, Out)
    if flag and T:
        print("YES")
        print(*[t + 1 for t in T])
    else:
        print("NO")


# Example call (you can change n for different scales)
if __name__ == "__main__":
    main(5)