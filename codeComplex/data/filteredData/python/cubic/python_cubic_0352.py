def main(n):
    # Map n to problem scale:
    # number of test cases T = max(1, n // 3)
    # for each test: N = n, K = min(20, max(1, n // 10))
    # A is a list of N integers in [1, base_n] deterministically generated
    T = max(1, n // 3)
    N = max(1, n)
    K = min(20, max(1, n // 10))

    # Precomputation upper bound for p-array
    base_n = max(10, N)

    squares = [i * i for i in range(1, int(base_n**0.5) + 2)]
    p = [i for i in range(base_n + 1)]
    for i in range(1, base_n + 1):
        if p[i] == i:
            for sq in squares:
                v = i * sq
                if v > base_n:
                    break
                p[v] = i

    results = []
    for t in range(T):
        # Deterministic generation of A of length N with values in [1, base_n]
        # example pattern: (i^2 + 3i + 7) % base_n + 1
        A_raw = [((i * i + 3 * i + 7 + 11 * t) % base_n) + 1 for i in range(N)]
        A = [p[a] for a in A_raw]

        dp = [N] * (K + 1)
        dp[0] = 1
        used = [set() for _ in range(K + 1)]
        for a in A:
            for j in range(K, -1, -1):
                if dp[j] == N:
                    continue
                if a in used[j]:
                    if j < K and dp[j + 1] > dp[j]:
                        dp[j + 1] = dp[j]
                        used[j + 1] = set(used[j])
                    dp[j] += 1
                    used[j] = set([a])

                else:
                    used[j].add(a)
        results.append(min(dp))

    # For time complexity experiments, we can return the last result or all results
    return results[-1] if results else None


if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    # print(main(1000))
    pass