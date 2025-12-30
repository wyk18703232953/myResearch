import random

def main(n: int):
    # 1. 生成测试数据：n 对 (l, r)
    # 这里简单生成 1 <= l <= r <= 10*n 的随机区间
    intervals = []
    for _ in range(n):
        l = random.randint(1, 10 * n)
        r = random.randint(l, 10 * n)
        intervals.append((l, r))

    # 2. 原始逻辑开始
    a = []
    for i in range(1, n + 1):
        l, r = intervals[i - 1]
        a.append([l, -r, i])
    a.sort()
    hh = a[0][1]
    wahh = max(-1, a[0][2])
    for i in range(1, n):
        if a[i][1] >= hh:
            print(a[i][2], wahh)
            return
        else:
            hh = a[i][1]
            wahh = a[i][2]
    print(-1, -1)


if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)