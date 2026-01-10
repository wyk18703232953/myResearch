def max_profit(n, k, l, d):
    a = []
    p, i = 0, -1
    while len(a) != k - 1:
        p += 1
        i += 1
        if l[i] in d:
            a.append(p)
            p = 0
            d.remove(l[i])
    a.append(n - sum(a))
    print(*a)


def main(n):
    if n <= 0:
        return
    # Define k based on n, ensure 1 <= k <= n
    k = max(1, min(n, n // 3 if n >= 3 else 1))
    l = [i % 10 for i in range(n)]
    d = sorted(l, reverse=True)[:k]
    print(sum(d))
    max_profit(n, k, l, d)


if __name__ == "__main__":
    main(10)