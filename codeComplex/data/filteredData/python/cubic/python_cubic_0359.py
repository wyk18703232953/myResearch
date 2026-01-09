def main(n):
    # Precompute p up to n
    squares = [i * i for i in range(1, int(n ** 0.5) + 2)]
    p = list(range(n + 1))
    for i in range(1, n + 1):
        if p[i] == i:
            for sq in squares:
                if i * sq > n:
                    break
                p[i * sq] = i

    # Deterministically construct a single test case
    # Map n to N, K, and array A
    if n < 3:
        N = 3

    else:
        N = n
    K = max(1, N // 10)

    # Generate raw values and map through p
    # Values are in [1, N], cyclic via modulo
    A_raw = [i % N + 1 for i in range(N)]
    A = [p[a] for a in A_raw]

    # Core algorithm (single test case)
    dp = [N] * (K + 1)
    dp[0] = 1
    used = [{} for _ in range(K + 1)]
    for a in A:
        for j in range(K, -1, -1):
            if dp[j] == N:
                continue
            if a in used[j]:
                if j < K and dp[j + 1] > dp[j]:
                    dp[j + 1] = dp[j]
                    used[j + 1] = dict(used[j])
                dp[j] += 1
                used[j] = {}
            used[j][a] = 1

    result = min(dp)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10**5)