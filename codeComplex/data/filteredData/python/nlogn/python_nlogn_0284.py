import random

def main(n):
    # 生成测试数据
    # n: 初始字典中的元素个数
    # m: 更新操作次数（这里设为 n，也可自行调整策略）
    m = n

    # 生成 n 个互不相同的索引和对应的值
    # 为了简单，这里索引取 1..2n 中的 n 个不重复数，值取 1..100
    indices_initial = random.sample(range(1, 2 * n + 1), n)
    values_initial = [random.randint(1, 100) for _ in range(n)]

    # 生成 m 个更新操作，同样在 1..2n 范围内随机索引和值
    indices_update = [random.randint(1, 2 * n) for _ in range(m)]
    values_update = [random.randint(1, 100) for _ in range(m)]

    # 原逻辑开始
    d = {}
    sm = 0

    # 模拟读入 n 对 (indx, y)
    for indx, y in zip(indices_initial, values_initial):
        d[indx] = y
        sm += y

    # 模拟读入 m 对 (indx, y) 进行更新
    for indx, y in zip(indices_update, values_update):
        if indx in d:
            sm -= d[indx]
            sm += max(y, d[indx])
        else:
            sm += y

    print(sm)


if __name__ == "__main__":
    # 例子：调用 main(5) 测试
    main(5)