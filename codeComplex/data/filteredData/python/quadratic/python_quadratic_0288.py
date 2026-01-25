def main(n):
    # generate deterministic input list l of length 2*n
    # pattern: l[i] = i % n, so each value 0..n-1 appears exactly twice
    l = [i % n for i in range(2 * n)]
    ans = 0
    m = []
    for i in range(2 * n - 1, -1, -1):
        if l[i] not in m:
            m.append(l[i])

    for tt in range(0, n):
        i = m[tt]
        j = l.index(i)
        l.pop(j)
        k = l.index(i)
        l.insert(k, j)
        ans += k - j
    print(ans)


if __name__ == "__main__":
    # example call; adjust n as needed for experiments
    main(5)