def main(n):
    # Map n to problem parameters
    k = max(1, n // 3)
    n = max(1, n)

    # Deterministic generation of a and t based on n
    a = [(i * 7 + 3) % 1000 + 1 for i in range(n)]
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
    for i in range(0, n - k + 1):
        m = max(m, cf[i + k] - cf[i])
    # print(ans + m)
    pass
if __name__ == "__main__":
    main(10)