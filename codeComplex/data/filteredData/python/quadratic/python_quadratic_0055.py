def main(n):
    # Map n to problem parameters
    N = n
    Q = n

    # Deterministic generation of array A of length N
    # Example: A[i] = (i * 7 + 3) % (N + 5)
    A = [(i * 7 + 3) % (N + 5) for i in range(N)]

    # Deterministic generation of Q queries (l, r), 0-based indices
    # Ensure 0 <= l <= r < N
    queries = []
    for i in range(Q):
        l = i % N
        r = (N - 1 - (i * 3 % N))
        if l > r:
            l, r = r, l
        queries.append((l, r))

    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] > A[j]:
                cnt += 1

    cnt %= 2

    Ans = [None] * Q
    for qu in range(Q):
        l, r = queries[qu]
        length = r - l + 1
        if (length * (length - 1) // 2) & 1:
            cnt ^= 1
        Ans[qu] = 'odd' if cnt else 'even'

    # print('\n'.join(Ans))
    pass
if __name__ == "__main__":
    main(1000)