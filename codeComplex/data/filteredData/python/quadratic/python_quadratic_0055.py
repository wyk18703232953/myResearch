def main(n):
    # n controls the size of the array N and the number of queries Q
    if n <= 0:
        return

    N = n
    Q = n

    # Deterministically generate array A of length N
    # Example pattern: A[i] = (i * 3) % (N + 1)
    A = [(i * 3) % (N + 1) for i in range(N)]

    # Precompute initial inversion parity
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] > A[j]:
                cnt += 1

    cnt %= 2

    # Deterministically generate Q queries (l, r), 1-based inclusive
    # Map n to intervals spread across [1, N]
    queries = []
    for k in range(Q):
        # Create a simple deterministic pattern for l and r
        l = (k * 2) % N + 1
        r = (k * 3) % N + 1
        if l > r:
            l, r = r, l
        queries.append((l, r))

    Ans = [None] * Q
    current_cnt = cnt
    for qu in range(Q):
        l, r = queries[qu]
        length = r - l + 1
        # Apply same logic as original code
        if (length * (length - 1) // 2) & 1:
            current_cnt ^= 1

        Ans[qu] = 'odd' if current_cnt else 'even'

    print('\n'.join(Ans))


if __name__ == "__main__":
    main(5)