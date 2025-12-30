from collections import defaultdict
import random

def main(n: int):
    # 生成一棵有 n 个节点的随机树，根节点为 1
    graph = defaultdict(list)
    par = [0] * (n + 1)  # par[i] 是节点 i 的父亲，par[1] 保留为 0 或自身
    for i in range(2, n + 1):
        p = random.randint(1, i - 1)  # 保证是树结构
        par[i] = p
        graph[p].append(i)

    bulb = [1] * (n + 1)
    # 根据父节点数组设置非叶子为 0
    for i in range(2, n + 1):
        bulb[par[i]] = 0

    # 自底向上累加子树叶子数
    for i in range(n, 0, -1):
        if bulb[i] == 0:
            count = 0
            for j in graph[i]:
                count += bulb[j]
            bulb[i] = count

    result = sorted(bulb[1:])
    print(' '.join(map(str, result)))


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)