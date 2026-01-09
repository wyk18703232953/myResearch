def main(n):
    # Map n to problem parameters deterministically
    # For scalability: let original n = n, m = max(1, n//3), k = n//4
    orig_n = max(1, n)
    m = max(1, orig_n // 3)
    k = orig_n // 4

    # Generate array a of length orig_n deterministically
    # Example pattern: a[i] = (i % 7) - 3
    a = [(i % 7) - 3 for i in range(orig_n)]

    n_val = orig_n
    dp = [-1] * (n_val + 15)
    for i in range(n_val):
        s = a[i]
        mx = max(0, a[i])
        for j in range(i - 1, max(-1, i - m), -1):
            s += a[j]
            mx = max(mx, s)
        if i - m >= 0:
            dp_prev = dp[i - m]

        else:
            dp_prev = 0
        dp[i] = max(0, dp_prev + s - k, mx - k)
    result = max(dp)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)