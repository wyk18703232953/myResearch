def main(n):
    # Deterministic data generation
    if n <= 0:
        # print(0)
        pass
        return

    # Set k as a deterministic function of n, ensure 1 <= k <= n
    k = max(1, n // 3)
    if k > n:
        k = n

    # Generate a deterministically varying array a
    a = [(i * 7 + 3) % 100 + 1 for i in range(n)]

    # Generate a deterministic pattern for t (0/1 flags)
    # Example: alternating blocks of 1s and 0s with length depending on i
    t = [((i // 3) % 2) for i in range(n)]

    p = [0] * (n + 1)
    now = 0
    for i in range(n):
        if t[i] == 1:
            now += a[i]
        p[i + 1] = p[i]
        if t[i] == 0:
            p[i + 1] += a[i]

    s = 0
    for i in range(n - k + 1):
        s = max(s, p[i + k] - p[i])

    # print(now + s)
    pass
if __name__ == "__main__":
    main(10)