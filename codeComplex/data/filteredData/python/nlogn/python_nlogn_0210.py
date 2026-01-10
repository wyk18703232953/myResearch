def main(n):
    # n: number of items; k is chosen deterministically as a function of n
    # Original input structure:
    # n, k
    # then n lines of: a, t
    #
    # Here we deterministically generate:
    # a_i = (i % n) + 1      (range from 1 to n)
    # t_i = (i * 2) % (n + 5) + 1  (some varying cost)
    # k   = n * (n + 1) // 4 (scales ~ n^2)
    if n <= 0:
        print(0)
        print(0)
        print()
        return

    k = n * (n + 1) // 4

    b = []
    for i in range(n):
        a = (i % n) + 1
        t = (i * 2) % (n + 5) + 1
        b.append([a, t, i + 1])

    b.sort(key=lambda x: x[1])

    d = {}
    e = {}
    ans = 0
    j = 0
    curr = 1
    currsum = 0
    l = 0
    while curr <= n:
        if curr - 1 in d:
            currsum -= d[curr - 1]
            l -= e[curr - 1]

        while j < n:
            if b[j][0] >= curr:
                currsum += b[j][1]
                if b[j][0] in d:
                    d[b[j][0]] += b[j][1]
                    e[b[j][0]] += 1
                else:
                    d[b[j][0]] = b[j][1]
                    e[b[j][0]] = 1
                l += 1
            if l == curr:
                j += 1
                break
            j += 1

        if j <= n and l == curr and currsum <= k:
            ans += 1
        else:
            break
        curr += 1

    c = []
    j = 0
    l = 0
    while j < n:
        if l == ans:
            break
        if b[j][0] >= ans:
            c.append(b[j][2])
            l += 1
        j += 1

    print(ans)
    print(ans)
    if c:
        print(*c)
    else:
        print()


if __name__ == "__main__":
    main(10)