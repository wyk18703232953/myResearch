def main(n):
    from collections import Counter, defaultdict
    import random

    d = defaultdict(int)
    for _ in range(n):
        u = random.randint(0, n)
        v = random.randint(u, n * 2)
        d[u] += 1
        d[v + 1] -= 1
    ks = sorted(d.keys())
    ks_n = len(ks)
    for i in range(1, ks_n):
        d[ks[i]] += d[ks[i - 1]]
    l = Counter()
    for i in range(ks_n - 1):
        times = d[ks[i]]
        cnt = ks[i + 1] - ks[i]
        l[times] += cnt
    res = []
    for i in range(1, n + 1):
        res.append(l[i])
    return res

if __name__ == "__main__":
    print(main(5))