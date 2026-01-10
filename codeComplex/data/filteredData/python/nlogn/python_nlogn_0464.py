def max_profit(n, k, l, d):
    a = []
    s, p, i = 0, 0, -1
    while len(a) != k - 1:
        p += 1
        i += 1
        if l[i] in d:
            s += l[i]
            a.append(p)
            p = 0
            d.remove(l[i])
    print(s + d[0])
    a.append(n - sum(i for i in a))
    print(*a)


def main(n):
    # Interpret n as the length of list l
    # We also need k, the number of largest elements to consider.
    # Define k deterministically as max(1, n//5) but not more than n.
    if n <= 0:
        return
    k = max(1, n // 5)
    if k > n:
        k = n

    # Deterministically generate l of length n
    # Example pattern: l[i] = (i * 7) % (n + 3) + 1
    l = [((i * 7) % (n + 3)) + 1 for i in range(n)]

    m = []
    m[:] = l[:]
    d = []
    m.sort(reverse=True)
    for i in range(k):
        d.append(m[i])
    max_profit(n, k, l, d)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(1000)