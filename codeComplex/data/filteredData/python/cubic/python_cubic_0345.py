import random

MOD = 10**9 + 7

# Precompute smallest "square-free core" representative up to MAXA
MAXA = 10**7
squares = {i * i for i in range(1, 4000)}

p = [i for i in range(MAXA + 1)]
for i in range(1, MAXA + 1):
    if p[i] == i:
        for sq in squares:
            v = i * sq
            if v > MAXA:
                break
            p[v] = i


def solve_single(N, K, A):
    # Transform A to their representatives via p[]
    A = [p[x] for x in A]

    dp = [N] * (K + 1)
    dp[0] = 0
    used = [set() for _ in range(K + 1)]

    for i in range(N):
        for j in range(K, -1, -1):
            if dp[j] == N:
                continue
            if A[i] in used[j]:
                # Need a new segment
                if j < K and dp[j + 1] > dp[j]:
                    dp[j + 1] = dp[j]
                    used[j + 1] = set(used[j])  # copy the set
                dp[j] += 1
                used[j] = {A[i]}
            else:
                used[j].add(A[i])

    return min(dp) + 1


def main(n):
    """
    n: scale parameter controlling generated test size.
    We generate:
      - T test cases
      - For each test:
          N, K = O(n) (bounded so that values stay reasonable)
          A[i] in [1, MAXA]
    Then we print the answer for each test.
    """
    random.seed(0)

    # Number of test cases
    T = max(1, n // 3)

    print(T)
    for _ in range(T):
        # Keep N, K moderate and <= n
        N = max(1, min(n, 20 + n // 2))
        K = random.randint(0, min(20, n))

        # Generate random A in [1, MAXA]
        A = [random.randint(1, MAXA) for _ in range(N)]

        print(N, K)
        print(" ".join(map(str, A)))
        # Compute and print result
        ans = solve_single(N, K, A)
        print(ans)


if __name__ == "__main__":
    # Example: call main with some scale, e.g., n = 50
    main(50)