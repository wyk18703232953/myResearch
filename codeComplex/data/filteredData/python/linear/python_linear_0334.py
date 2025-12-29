import random

def main(n: int):
    # 1. 生成测试数据
    # 保证有 n 个断点在区间 (0, m) 内，递增且不重复
    # 设置 m 与 n 同阶，这里取 m = 10 * n + 10，避免太小
    if n <= 0:
        # 边界情况：没有内部断点
        m = 10
        w = [0, m]
    else:
        m = 10 * n + 10
        # 从 1 到 m-1 中随机取 n 个点并排序
        inner_points = random.sample(range(1, m), n)
        inner_points.sort()
        w = [0] + inner_points + [m]

    # 2. 按原逻辑计算答案
    # 注意：原代码在读入后做了 w = [0] + w + [m]，这里已直接构造好

    c, d = [], []
    res = 0

    # 前缀部分 c
    for j in range(n + 1):
        c.append(res)
        if j % 2 == 0:
            res += w[j + 1] - w[j]

    # 后缀部分 d
    res = 0
    for j in range(n + 1, -1, -1):
        if j % 2 == 0 and j != n + 1:
            res += w[j + 1] - w[j]
        d.append(res)
    d = d[::-1]

    # 求最大值 mx
    mx = d[0]
    for j in range(n + 1):
        mx = max(
            c[j] + (w[j + 1] - w[j] - 1) + (m - w[j + 1] - d[j + 1]),
            mx
        )

    print(mx)


if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)