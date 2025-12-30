from collections import defaultdict
import random

def main(n: int):
    # 1. 生成测试数据（随机生成一棵以 1 为根的树的父节点数组 par）
    # par[i] 表示节点 i+2 的父节点（原代码中 par 长度为 n-1，对应节点 2..n）
    if n < 1:
        return

    graph = defaultdict(list)
    par = []

    # 生成一棵树：对于每个节点 2..n，随机选择 [1, i] 范围内的一个父节点
    # 保证有根且无环
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        par.append(parent)
        graph[parent].append(i)

    # 2. 原逻辑开始
    bulb = [1] * (n + 1)
    for i in range(n - 1):
        bulb[par[i]] = 0
        # graph 已在上面构建，这里理论上可以省略，但保留与原逻辑一致
        # graph[par[i]].append(i + 2)

    zero = bulb.count(0)  # 变量 zero 在原代码中未使用，这里保留计算

    # 自底向上更新 bulb 值
    for i in range(n, 0, -1):
        if bulb[i] == 0:
            count = 0
            for j in graph[i]:
                count += bulb[j]
            bulb[i] = count

    bulb = bulb[1:]
    bulb.sort()
    print(' '.join(map(str, bulb)))


if __name__ == "__main__":
    # 这里可以修改 n 以进行不同规模的测试
    main(10)