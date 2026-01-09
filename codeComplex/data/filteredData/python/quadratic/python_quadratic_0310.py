def main(n):
    import math

    # Map n to problem size: choose k and build list l of length n
    # Ensure k >= 1 and k <= n (for n >= 1)
    if n <= 0:
        return 0.0

    # Deterministic choice for k: roughly n//3 (at least 1)
    k = max(1, n // 3)

    # Deterministic array generation
    # Example pattern: l[i] = (i % 7) - 3  (includes positive, zero, negative)
    l = [(i % 7) - 3 for i in range(n)]

    ans = float("-inf")
    for i in range(n):
        c = 0
        sum1 = 0
        for j in range(i, n):
            sum1 += l[j]
            c += 1
            if c >= k:
                ans = max(ans, sum1 / c)

    # For experimental use, we print the result
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)