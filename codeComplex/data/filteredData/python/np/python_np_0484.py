def main(n):
    import collections

    # Scale design:
    # K = 3 (matches original 2**K pattern generation)
    # number of strings n
    # number of rules m = n (for simplicity, one rule per string)
    K = 3
    m = n

    # Deterministic generation of A: all strings of length K over 'a','b','c'
    # but limited to first n strings in lexicographical order
    chars = ['a', 'b', 'c']
    A = []
    for i in range(n):
        s = []
        x = i
        for _ in range(K):
            s.append(chars[x % 3])
            x //= 3
        A.append(''.join(s))
    # In case n == 0
    if n == 0:
        print("YES")
        print()
        return

    # Deterministic generation of B:
    # Each rule uses a pattern derived from A[i] with some '_' positions
    # and maps to index (i % n) + 1
    B = []
    for i in range(m):
        pattern_chars = list(A[i % n])
        # Add '_' on deterministic positions: every second position
        for k in range(K):
            if (i + k) % 2 == 0:
                pattern_chars[k] = '_'
        pattern = ''.join(pattern_chars)
        b = (i % n) + 1
        B.append([pattern, str(b)])

    alpha = 'abcｄ'

    D = dict()
    for i, x in enumerate(A):
        D[x] = i

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
    s = set()
    q = collections.deque()
    for i in range(n):
        if X[i] == 0:
            q.append(i)
            s.add(i)

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