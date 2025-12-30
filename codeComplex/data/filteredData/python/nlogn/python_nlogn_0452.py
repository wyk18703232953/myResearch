import random

def main(n):
    MAXN = 200001
    # 随机生成测试数据：
    # 1. 随机选择 m 为 1..n 之间的某个值（也可改为固定值）
    # 2. 生成长度为 n 的数组 s，元素范围控制在 [-100000, 100000]
    m = random.randint(1, max(1, n))
    s = [random.randint(-10**5, 10**5) for _ in range(n)]

    f = [0 for _ in range(n + 1)]
    # count 下标需要从 -MAXN 到 MAXN
    base = MAXN  # 映射：value v -> index v + base
    count = [0 for _ in range(2 * MAXN + 1)]

    f[0] = 0
    last = 0
    res = 0

    for i in range(1, n + 1):
        if s[i - 1] == m:
            for j in range(last, i):
                count[f[j] + base] += 1
            last = i

        if s[i - 1] > m:
            f[i] = f[i - 1] - 1
        else:
            f[i] = f[i - 1] + 1

        res += count[f[i] + base] + count[f[i] - 1 + base]

    print(res)


if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)