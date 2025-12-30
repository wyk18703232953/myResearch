import random

def main(n):
    # 生成测试数据：
    # a 随机 [0, 10^4]，b 随机 [1, 10^4] 且 b > a
    # d 为严格递增且在 (a, b) 内的 n 个整数
    a = random.randint(0, 10000)
    b = random.randint(a + 1, a + 10000)

    # 在 (a, b) 间选 n 个不同点（若区间不足则压缩 n）
    max_points = max(0, b - a - 1)
    n = min(n, max_points)
    if n > 0:
        d = sorted(random.sample(range(a + 1, b), n))
    else:
        d = []

    # 原逻辑开始
    e = []
    e1 = []
    mx = 0
    current = a
    for i in range(len(d)):
        if i % 2 == 0:
            e.append(d[i] - current)
        else:
            e1.append(d[i] - current)
        current = d[i]
    if len(d) == 0:
        # 原代码中 i 不存在，此处直接补上尾段
        e.append(b - current)
    else:
        if i % 2 == 0:
            e1.append(b - current)
        else:
            e.append(b - current)

    mx = sum(e)
    su = 0
    su2 = sum(e1)
    for i in range(len(e)):
        su += e[i]
        mx = max(mx, su + su2 - 1)
        try:
            su2 -= e1[i]
        except IndexError:
            break

    print(mx)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)