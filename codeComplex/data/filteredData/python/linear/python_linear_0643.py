import random

def main(n: int):
    # 生成测试数据：构造一个长度为 n 的数组 a
    # 要求能覆盖原算法逻辑：
    # 1. 随机生成若干个 a[i] == 1 的叶子节点
    # 2. 其余位置生成 a[i] != 1 的值（尽量保证 sum(root_r) >= len(leaf) 的概率较高）
    #
    # 这里采用：随机生成 [1, n] 的整数，其中一部分人为设置为 1
    if n <= 0:
        return

    # 基础随机数组
    a = [random.randint(2, n + 1) for _ in range(n)]

    # 随机选取若干个位置设为 1，确保至少有 1 个叶子（若 n>=1）
    leaf_count = random.randint(1, max(1, n // 2))  # 控制叶子数量不太大
    leaf_positions = random.sample(range(n), leaf_count)
    for pos in leaf_positions:
        a[pos] = 1

    # 下面是原始逻辑
    leaf = [i + 1 for i in range(n) if a[i] == 1]
    root_w = [i + 1 for i in range(n) if a[i] != 1]
    root_r = [a[i - 1] - 2 for i in root_w]

    l_path = root_w[:]
    if len(leaf) != 0:
        l_path = [leaf[0]] + l_path
        leaf = leaf[1:]
    if len(leaf) != 0:
        l_path = l_path + [leaf[0]]
        leaf = leaf[1:]

    if sum(root_r) < len(leaf):
        print("NO")
    else:
        print("YES {}".format(len(l_path) - 1))
        print(n - 1)
        for i in range(len(l_path) - 1):
            print("{} {}".format(l_path[i], l_path[i + 1]))
        for l in leaf:
            while len(root_r) > 0 and root_r[0] == 0:
                root_w = root_w[1:]
                root_r = root_r[1:]
            print("{} {}".format(l, root_w[0]))
            root_r[0] = root_r[0] - 1


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)