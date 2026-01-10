def main(n):
    # n: length of array a
    if n < 2:
        print(-1)
        return

    # Deterministic generation of m and array a
    # m grows with n, but always positive
    m = max(1, n // 3)
    a = [i * 2 for i in range(n)]

    k = 0
    ans = -1
    for i in range(n - 1):
        while k < n - 1 and a[k + 1] - a[i] <= m:
            k += 1
        if i < k - 1:
            num = a[k] - a[i + 1]
            den = a[k] - a[i]
            ans = max(ans, num / den)
    print(ans)


if __name__ == "__main__":
    main(10)