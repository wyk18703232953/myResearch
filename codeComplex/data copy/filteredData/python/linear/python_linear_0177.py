def main(n):
    if n <= 0:
        return 0
    # Define window size k based on n, ensure 1 <= k <= n
    k = max(1, n // 3)
    if k > n:
        k = n

    # Deterministically generate arrays a and t based on n
    a = [(i * 2 + 1) for i in range(n)]
    t = [1 if (i % 3 == 0) else 0 for i in range(n)]

    ans = 0
    m = 0
    for i in range(n):
        if t[i]:
            ans += a[i]
            a[i] = 0
    cf = [0] * (n + 1)
    for i in range(1, n + 1):
        cf[i] = cf[i - 1] + a[i - 1]
    for i in range(n - k + 1):
        m = max(m, cf[i + k] - cf[i])
    result = ans + m
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)