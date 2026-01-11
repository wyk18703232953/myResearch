def main(n):
    # Deterministically generate k based on n, ensure k >= 2
    k = max(2, n + 7)

    # Generate n numbers as strings; length varies with i to keep l[i] meaningful
    # Example: a[i] is the string representation of i * (i + 1)
    a = [str(i * (i + 1)) for i in range(1, n + 1)]

    mods = [dict() for _ in range(10)]
    l = [0] * n

    for i in range(n):
        l[i] = len(a[i])
        a[i] = int(a[i]) % k
        cur = a[i]
        for j in range(10):
            cur = cur * 10 % k
            mods[j][cur] = mods[j].get(cur, 0) + 1

    ans = 0
    for i in range(n):
        mod = (k - a[i]) % k
        ans += mods[l[i] - 1].get(mod, 0)
        cur = a[i]
        for _ in range(l[i]):
            cur = cur * 10 % k
        if cur == mod:
            ans -= 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)