def main(n):
    # In the original problem, there are two inputs: n and s.
    # Here we deterministically construct s from n.
    # We choose s so that 1 <= s <= n, using a simple deterministic rule.
    s = max(1, n // 2)

    l = s
    h = n
    ans = n + 1

    while l <= h:
        m = (l + h) // 2
        t = 0
        for ch in str(m):
            t += int(ch)
        if m - t >= s:
            ans = m
            h = m - 1

        else:
            l = m + 1

    result = n - ans + 1
    if result < 0:
        result = 0
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10**6)