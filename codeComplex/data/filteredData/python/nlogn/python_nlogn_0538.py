def main(n):
    # Deterministically generate k and array a based on n
    # Ensure k >= 2 to avoid division/modulo by zero
    k = max(2, n + 7)
    a = [(i * 1234567 + 89) % (10**12) + 1 for i in range(n)]

    rda = []
    for j in range(12):
        rd = dict()
        x = pow(10, j)
        for i in range(n):
            r = (a[i] * x) % k
            rd[r] = rd.setdefault(r, 0) + 1
        rda.append(rd)

    ans = 0
    for i in range(n):
        r = a[i] % k
        ln = len(str(a[i]))
        x = pow(10, ln)
        if r == 0:
            r = k
        if k - r in rda[ln]:
            ans += rda[ln][k - r]
            if (a[i] * x) % k == k - r:
                ans -= 1
    print(ans)


if __name__ == "__main__":
    main(10000)