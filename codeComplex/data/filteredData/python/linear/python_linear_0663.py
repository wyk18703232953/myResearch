import random

def main(n: int):
    # 1. 生成测试数据
    # 随机生成一棵 n 个节点的树
    # 节点编号为 1..n
    edges = []
    for i in range(2, n + 1):
        # 随机连接到一个已有节点，形成一棵树
        parent = random.randint(1, i - 1)
        edges.append((parent, i))

    # 随机生成 s（可根据需要调整范围，这里设为 1~10^6）
    s = random.randint(1, 10**6)

    # 2. 原逻辑计算
    l = [0 for _ in range(n)]
    for a, b in edges:
        l[a - 1] += 1
        l[b - 1] += 1

    count = 0
    for i in range(n):
        if l[i] == 1:
            count += 1

    # 为避免除零情况，这里做个保护；若无叶子，则结果设为 0.0
    if count == 0:
        result = 0.0
    else:
        result = (s / count) * 2

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)