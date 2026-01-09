def main(n):
    import math

    # Precompute f as in original code
    f = [0] * 100
    for i in range(100):
        f[i] = (4**i - 1) // 3

    def solve(N, K):
        if N < 100 and f[N] < K:
            # print('NO')
            pass
            return

        for i in range(99):
            if f[i] <= K < f[i + 1]:
                x = K - f[i]
                a = N - i

                if x == 0:
                    # print('YES {}'.format(a))
                    pass
                    return

                edge = 2**(i + 1) - 1
                others = (2**i - 1) ** 2
                if edge == x:
                    # print('YES {}'.format(a - 1))
                    pass
                    return

                ans = a
                if edge < x:
                    x -= edge
                    ans = a - 1

                # split others
                for j in range(a + 1):
                    if others * f[j] >= x:
                        # print('YES {}'.format(ans))
                        pass
                        return
                # print('NO')
                pass
                return

        # print('NO')
        pass

    # Deterministic test generation:
    # Interpret n as number of test cases T.
    # For each test case t (0-based), generate:
    #   N_t in [1, 150]
    #   K_t derived deterministically from t and N_t.
    T = n
    for t in range(T):
        N = 1 + (t % 150)
        # Produce a mix of K values relative to f to exercise branches
        if N < 100:
            base = f[N]

        else:
            base = f[99]

        mode = t % 4
        if mode == 0:
            K = base  # K == f[N] or f[99]
        elif mode == 1:
            K = base // 2  # smaller than base
        elif mode == 2:
            K = base + (t // 2 + 1)  # slightly larger

        else:
            K = base + (t + 1) * (t + 2)  # larger growth

        solve(N, K)


if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)