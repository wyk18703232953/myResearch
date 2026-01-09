def main(n):
    l = [-1] * n
    r = [-1] * n
    # Deterministically generate a of length 2n with values in [1, n]
    # Pattern: 1,2,...,n,1,2,...,n
    a = [(i % n) + 1 for i in range(2 * n)]
    for i in range(2 * n):
        x = a[i] - 1
        if l[x] == -1:
            l[x] = i
        r[x] = i
    ans = 0
    for i in range(n):
        for j in range(n):
            if l[i] < l[j] < r[j] < r[i]:
                ans += 2
    for i in range(n):
        ans += r[i] - l[i] - 1
    # print(ans // 2)
    pass
if __name__ == "__main__":
    main(10)