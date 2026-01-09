def main(n):
    # Interpret n as the size of the original array 'a'
    # Generate deterministic test data:
    # a will be a strictly increasing sequence within [1, m-1]
    # Let m be a simple function of n to keep scales related.
    if n <= 0:
        return 0

    m = 3 * n + 5
    # Ensure elements are within [1, m-1] and strictly increasing
    # Example: a[i] = 1 + (i * 2) % (m - 1), then make it strictly increasing
    base = [(1 + (i * 2)) % (m - 1) for i in range(n)]
    base[0] = max(1, base[0])
    for i in range(1, n):
        if base[i] <= base[i - 1]:
            base[i] = base[i - 1] + 1
        if base[i] >= m:
            base[i] = m - 1

    a = [0] + base + [m]
    n2 = len(a)
    suf = [0] * n2
    suf[n2 - 2] = abs(a[-2] - a[-1])
    for i in range(n2 - 3, -1, -1):
        suf[i] = a[i + 1] - a[i] + suf[i + 2]
    ans = suf[0]
    cost = 0
    for i in range(1, n2):
        if i & 1:
            v = a[i] - 1 - a[i - 1]
            if v != 0:
                ans = max(ans, cost + v + suf[i])
            cost += a[i] - a[i - 1]

        else:
            v = a[i - 1] + 1
            if v != a[i]:
                ans = max(
                    ans,
                    cost + a[i] - v + (suf[i + 1] if i + 1 < n2 else 0),
                )
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    main(10)