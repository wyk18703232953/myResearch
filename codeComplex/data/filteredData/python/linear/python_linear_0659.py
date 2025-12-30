import random

def main(n):
    # 随机生成总权值 s（例如 1 到 10^6）
    s = random.randint(1, 10**6)

    # 构造一棵含 n 个节点的随机树（保证连通且无环）
    # 使用随机的“父指针”方式生成树边
    degs = [0] * n
    edges = []
    for i in range(2, n + 1):
        # 随机选择 1..i-1 作为父节点
        parent = random.randint(1, i - 1)
        edges.append((parent, i))
        degs[parent - 1] += 1
        degs[i - 1] += 1

    # 原逻辑：计算度数为 1 的点的数量，并输出 2*s / 叶子数
    leaf_count = degs.count(1)
    # 为避免除零（理论上 n>=2 时树至少有2个叶子）
    if leaf_count == 0:
        result = 0.0
    else:
        result = 2 * s / leaf_count

    print(result)

if __name__ == "__main__":
    # 示例：以 n=10 运行
    main(10)