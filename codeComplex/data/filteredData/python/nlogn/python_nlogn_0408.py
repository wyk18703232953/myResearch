from collections import Counter, defaultdict
import random

def main(n):
    # 生成测试数据：n 个区间 [u, v]，1 <= u <= v <= n
    intervals = []
    for _ in range(n):
        u = random.randint(1, n)
        v = random.randint(u, n)
        intervals.append((u, v))

    d = defaultdict(int)
    for u, v in intervals:
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
        if times > 0:
            l[times] += cnt

    out = []
    for i in range(1, n + 1):
        out.append(str(l[i]))
    print(' '.join(out))


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)