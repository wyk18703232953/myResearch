def main(n):
    if n <= 1:
        n = 2

    q = n
    a = [(i % 5) + 1 for i in range(n)]

    def p(c_k, r, pr_a):
        l = 0
        while r - l > 1:
            z = (r + l) // 2
            if pr_a[z] > c_k:
                r = z
            else:
                l = z
        return l

    pr_a = []
    for i in range(n):
        pr_a.append(a[i])
        if i > 0:
            pr_a[i] += pr_a[i - 1]

    k = [(i % 7) + 1 for i in range(q)]
    c_k = 0
    ans = []
    for qq in range(q):
        c_k += k[qq]
        l = p(c_k, n - 1, pr_a)
        if pr_a[l] <= c_k:
            l += 1
        if c_k >= pr_a[n - 1]:
            c_k = 0
            l = 0
        ans.append(str(n - l))
    print('\n'.join(ans))


if __name__ == "__main__":
    main(10)