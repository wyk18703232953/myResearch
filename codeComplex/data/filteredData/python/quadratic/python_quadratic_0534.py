def main(n):
    # Interpret n as both the length of arrays and the number of markers (ones) in b
    # Ensure n >= 2 for meaningful behavior
    if n < 2:
        n = 2

    # Generate deterministic arrays a and b, and parameter m
    # a: increasing integers starting from 0
    a = [i for i in range(n)]

    # b: length n, exactly m ones at deterministic positions
    # Let m = max(1, n // 3)
    m = max(1, n // 3)
    if m > n:
        m = n

    b = [0] * n
    # Place ones at positions: floor(i * n / m), for i = 0..m-1
    for i in range(m):
        pos = (i * n) // m
        if pos >= n:
            pos = n - 1
        b[pos] = 1

    def next_pos(k, arr):
        i = k + 1
        while i < len(arr) and arr[i] != 1:
            i += 1
        return i

    ans = [0] * (m + 1)

    k = -1
    k = next_pos(k, b)
    if k >= n:
        # In case no 1 exists, just print zeros
        # print(" ".join(str(0) for _ in range(1, m + 1)))
        pass
        return

    ans[1] = k
    for i in range(2, m + 1):
        kk = next_pos(k, b)
        if kk >= n:
            kk = n - 1
        for j in range(k + 1, kk):
            if a[j] - a[k] <= a[kk] - a[j]:
                ans[i - 1] += 1

            else:
                ans[i] += 1
        k = kk

    ans[m] += (n + m - 1 - k)

    # print(" ".join(str(ans[i]) for i in range(1, m + 1)))
    pass
if __name__ == "__main__":
    main(10)