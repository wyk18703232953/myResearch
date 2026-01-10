def main(n):
    # Deterministically generate k and array a based on n
    # k is chosen as a positive integer >= 2
    k = (n % 1000) + 2

    # Generate n integers for array a
    # Example deterministic pattern: a[i] = (i * i + 3 * i + 7) % (10**9 + 7)
    MOD = 10**9 + 7
    a = [((i * i + 3 * i + 7) % MOD) for i in range(n)]

    sz = []
    t = [1] * 11

    cnt = dict()
    for i in range(n):
        sz.append(len(str(a[i])))
        tmp = (sz[i], a[i] % k)
        if tmp in cnt:
            cnt[tmp] += 1
        else:
            cnt[tmp] = 1

    t[0] = 1
    for i in range(1, 11):
        t[i] = (t[i - 1] * 10) % k

    ans = 0
    for i in range(n):
        for l in range(1, 11):
            cur = (k - a[i] * t[l]) % k
            tmp = (l, cur)
            if tmp in cnt:
                ans += cnt[tmp]
            if (sz[i] == l and cur == a[i] % k):
                ans -= 1

    print(ans)


if __name__ == "__main__":
    main(10)