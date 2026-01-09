def main(n):
    # Interpret n as the length of the array a
    # Deterministic construction of parameters and data
    m = max(1, n // 3)      # window size-like parameter
    k = n                   # constant added per step
    a = [None] + [i % 7 - 3 for i in range(1, n + 1)]  # values in [-3,3]

    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = p[i - 1] + a[i]

    s = [10 ** 16 for _ in range(m)]
    s[0] = k
    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, p[i] - min(s))
        idx = i % m
        if p[i] < s[idx]:
            s[idx] = p[i]
        s[idx] += k

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)