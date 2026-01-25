def main(n):
    # Interpret n as m (upper bound of the range), build a deterministic array a
    # Original code expects: first line "n m", second line list a of length n
    # Here we set n_data = n and m = n, and generate a[i] = i for i in [1..n]
    if n <= 0:
        return 0

    m = n
    a = list(range(1, n + 1))  # deterministic data of size n

    # Original logic below (non-interactive)
    a = [0] + a + [m]
    n = len(a)
    suf = [0] * n
    suf[n - 2] = abs(a[-2] - a[-1])
    for i in range(n - 3, -1, -1):
        suf[i] = a[i + 1] - a[i] + suf[i + 2]
    ans = suf[0]
    cost = 0
    for i in range(1, n):
        if i & 1:
            v = a[i] - 1 - a[i - 1]
            if v != 0:
                ans = max(ans, cost + v + suf[i])
            cost += a[i] - a[i - 1]
        else:
            v = a[i - 1] + 1
            if v != a[i]:
                ans = max(ans, cost + a[i] - v + (suf[i + 1] if i + 1 < n else 0))
    return ans


if __name__ == "__main__":
    # Example deterministic call for experimentation
    for size in [1, 2, 5, 10, 20]:
        print(size, main(size))