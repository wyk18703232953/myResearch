import sys
from collections import Counter, defaultdict

def main(n):
    d = defaultdict(int)
    for i in range(n):
        u = i
        v = i + (i % 5)
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
    out = []
    for i in range(1, n + 1):
        out.append(str(l[i]))
    sys.stdout.write(" ".join(out))

if __name__ == "__main__":
    main(10)