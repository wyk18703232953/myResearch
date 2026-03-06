def main(n):
    from collections import defaultdict, Counter, deque

    # Scale parameters deterministically based on n
    # n: number of patterns
    # m: number of strings/constraints
    # k: length of each pattern
    if n < 1:
        return

    k = max(1, n % 7 + 1)
    m = max(1, 2 * n)

    # Generate deterministic pattern strings P of length k
    alphabet = "abcd_efghijklmnopqrstuvwxyz"
    base = len(alphabet)

    P = []
    for i in range(n):
        s = []
        x = i + 1
        for j in range(k):
            s.append(alphabet[(x + j) % base])
        P.append("".join(s))

    # Generate deterministic S list: each element is [string, index]
    # Strings are constructed to have some relation to P to keep graph non-trivial
    S = []
    for t in range(m):
        base_idx = (t * 37) % n
        pattern = list(P[base_idx])
        # Modify up to one position deterministically
        pos = (t * 13) % k
        pattern[pos] = P[(base_idx + 1) % n][pos]
        s = "".join(pattern)
        # Choose i between 1..n such that it is related to base_idx
        i = (base_idx + (t % 3)) % n + 1
        S.append([s, str(i)])

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
            print("NO")
            break
        for c in cand:
            if c == i:
                continue
            G[i].append(c)
            deg[c] += 1
    else:
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
            print("NO")
        else:
            print("YES")
            print(*ans)


if __name__ == "__main__":
    main(10)