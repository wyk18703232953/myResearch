def main(n):
    import collections

    if n < 1:
        n = 1

    # K controls the pattern length; small constant to keep 2**K manageable
    K = 4

    # Generate n distinct pattern strings of length K using 'a'/'b'/'c'
    # Deterministic based on n and K.
    def idx_to_pattern(idx, length):
        chars = ['a', 'b', 'c']
        res = []
        for _ in range(length):
            res.append(chars[idx % 3])
            idx //= 3
        return ''.join(res)

    A = [idx_to_pattern(i, K) for i in range(n)]

    # Map patterns to indices
    D = {x: i for i, x in enumerate(A)}

    # Generate m constraint pairs; scale m with n
    # Each pair is (pattern_with_underscores, target_index_1_based)
    m = n * 2
    B = []
    for i in range(m):
        base_idx = i % n
        target = (i * 7 + 3) % n  # deterministic pseudo-mix
        base_pattern = A[base_idx]
        # Create an underscore mask pattern deterministically
        mask = []
        for k in range(K):
            # Use bits of (i + k) to decide underscore or not
            if ((i + k) // (k + 1)) % 2 == 0:
                mask.append('_')
            else:
                mask.append(base_pattern[k])
        masked = ''.join(mask)
        B.append([masked, str(target + 1)])

    G = [set() for _ in range(n)]
    X = [set() for _ in range(n)]

    for i in range(m):
        a, b = B[i]
        b = int(b)
        flag = False
        for j in range(2 ** K):
            x = []
            for k in range(K):
                if (j >> k) % 2 == 1:
                    x.append('_')
                else:
                    x.append(a[k])
            x = ''.join(x)
            if x in D:
                if D[x] == b - 1:
                    flag = True
                    continue
                else:
                    G[b - 1].add(D[x])
                    X[D[x]].add(b - 1)
        if flag:
            continue
        else:
            print("NO")
            return

    X = [len(X[i]) for i in range(n)]
    ANS = []
    q = collections.deque()
    for i in range(n):
        if X[i] == 0:
            q.append(i)
    while q:
        if len(ANS) == n:
            print("NO")
            return
        x = q.popleft()
        ANS.append(x + 1)
        for y in G[x]:
            if X[y] == 0:
                continue
            else:
                X[y] -= 1
                if X[y] == 0:
                    q.append(y)
    if len(ANS) == n:
        print("YES")
        print(*ANS)
    else:
        print("NO")


if __name__ == "__main__":
    main(10)