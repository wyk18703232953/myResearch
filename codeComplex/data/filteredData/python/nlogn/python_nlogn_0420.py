from collections import defaultdict
import random

def main(n: int):
    # 生成测试数据：n 个区间 [l, r]，保证 l <= r
    intervals = []
    for _ in range(n):
        l = random.randint(0, 10 * n)
        r = random.randint(l, l + random.randint(0, 10))  # 控制区间长度
        intervals.append((l, r))

    s = []
    for a0, a1 in intervals:
        s += [(a0, 0), (a1, 1)]
    s.sort()

    now, rev = 0, defaultdict(int)
    for a, b in zip(s, s[1:]):
        now += 1 if a[1] == 0 else -1
        if a[1] == 0:
            rev[now] += b[0] - a[0] + (1 if b[1] == 1 else 0)
        elif b[0] != a[0]:
            rev[now] += b[0] - a[0] - (1 if b[1] == 0 else 0)

    # 输出结果
    for i in range(1, n + 1):
        print(rev[i], end=" ")

if __name__ == "__main__":
    # 示例：n = 5
    main(5)