import sys
from collections import defaultdict, Counter, deque

def run_algorithm(n, m, k, P, S):
    idx = {p: i for i, p in enumerate(P, 1)}
    G = defaultdict(list)
    deg = Counter()
    for s, i in S:
        i = int(i)
        cand = set()
        for mask in range(1 << k):
            cur = ['_'] * k
            for j in range(k):
                if mask >> j & 1:
                    cur[j] = s[j]
            cur = "".join(cur)
            if cur in idx:
                cand.add(idx[cur])
        if i not in cand:
            return "NO", None
        for c in cand:
            if c == i:
                continue
            G[i].append(c)
            deg[c] += 1
    ans = []
    q = deque([i for i in range(1, n + 1) if not deg[i]])
    while q:
        i = q.popleft()
        ans.append(i)
        for j in G[i]:
            deg[j] -= 1
            if not deg[j]:
                q.append(j)
    if len(ans) < n:
        return "NO", None
    else:
        return "YES", ans

def generate_data(n):
    # Define deterministic sizes based on n
    k = max(1, min(10, n % 10 + 1))           # pattern length between 1 and 10
    num_patterns = max(1, n)                  # number of patterns P
    num_queries = max(1, 2 * n)               # number of queries S

    # Generate patterns P: deterministic underscore/letter patterns
    P = []
    for i in range(1, num_patterns + 1):
        chars = []
        for j in range(k):
            if (i + j) % 3 == 0:
                chars.append('_')
            else:
                # deterministic lower-case letter cycle
                letter = chr(ord('a') + ((i + j) % 26))
                chars.append(letter)
        P.append("".join(chars))

    # Ensure at least one fully matching pattern to avoid trivial NO
    base_pattern = []
    for j in range(k):
        letter = chr(ord('a') + (j % 26))
        base_pattern.append(letter)
    base_pattern = "".join(base_pattern)
    if base_pattern not in P:
        P[0] = base_pattern

    # Build S queries deterministically
    S = []
    for q in range(1, num_queries + 1):
        # choose a pattern index deterministically
        idx = (q % num_patterns) + 1
        pattern = P[idx - 1]
        # produce string s from pattern: replace '_' with deterministic letter
        s_chars = []
        for j, ch in enumerate(pattern):
            if ch == '_':
                s_chars.append(chr(ord('a') + ((q + j) % 26)))
            else:
                s_chars.append(ch)
        s = "".join(s_chars)
        S.append((s, str(idx)))

    return num_patterns, num_queries, k, P, S

def main(n):
    n = int(n)
    num_patterns, num_queries, k, P, S = generate_data(n)
    result, order = run_algorithm(num_patterns, num_queries, k, P, S)
    if result == "NO":
        print("NO")
    else:
        print("YES")
        print(*order)

if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(5)