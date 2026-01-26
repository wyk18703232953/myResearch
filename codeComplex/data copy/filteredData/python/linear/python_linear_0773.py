def main(n):
    # n controls the size of the generated input:
    # we generate n (number of elements), m, k and an array A of length m
    # in a fully deterministic way based on n.
    #
    # Original program expects:
    # n, m, k
    # A[0..m-1]
    #
    # Here we map:
    #   N = max(1, n)
    #   M = max(1, n // 2)
    #   K = max(1, n // 3)
    # and construct a strictly increasing A with values in [1, N].

    if n <= 0:
        N = 1
        M = 1
        K = 1

    else:
        N = n
        M = max(1, n // 2)
        K = max(1, n // 3)

    # Build a strictly increasing sequence A within 1..N.
    A = []
    if M >= N:
        # If requested length is >= N, just use 1..N
        A = list(range(1, N + 1))
        M = N

    else:
        # Spread M values in 1..N deterministically
        step = max(1, N // (M + 1))
        cur = 1
        for _ in range(M):
            if cur > N:
                cur = N
            A.append(cur)
            cur += step
        # Ensure strictly increasing and within bounds
        A = sorted(set(min(max(1, x), N) for x in A))
        M = len(A)

    n_val = N
    m_val = M
    k_val = K

    # Core logic from original code, unchanged except using generated values
    n, m, k = n_val, m_val, k_val
    A.append(n + 1)
    COMP = []
    NOW = 0
    for a in A:
        if a - NOW - 1 != 0:
            if a - NOW - 1 > 2 * k:
                COMP.append([(a - NOW - 1) % k + k, 0])

            else:
                COMP.append([a - NOW - 1, 0])
        COMP.append([1, 1])
        NOW = a

    COMP.pop()

    ANS = 0
    NOW_PAGE = 0
    NOW_SCORE = 0

    pa = 0
    LEN = len(COMP)
    while pa < LEN:
        i, j = COMP[pa]

        if NOW_PAGE + i <= k:
            NOW_PAGE += i
            NOW_SCORE += j
            pa += 1

        else:
            if NOW_SCORE > 0:
                COMP[pa][0] -= k - NOW_PAGE
                NOW_PAGE = k - NOW_SCORE

                ANS += 1
                NOW_SCORE = 0

            else:
                if NOW_PAGE == k:
                    NOW_PAGE = 0

                else:
                    COMP[pa][0] -= k - NOW_PAGE
                    NOW_PAGE = k - NOW_SCORE

    if NOW_SCORE > 0:
        ANS += 1

    # print(ANS)
    pass
if __name__ == "__main__":
    # Example deterministic call; change n to vary input scale.
    main(100)