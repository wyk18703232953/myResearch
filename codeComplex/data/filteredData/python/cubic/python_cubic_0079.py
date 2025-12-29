from queue import Queue
import random


def main(n):
    # 生成测试数据：
    # 给定规模 n，令 m = n，k 为树的数量，随机在 n x m 网格中生成 k 个树的位置
    m = n
    # 至少 1 棵树，至多 n（可按需调整规模策略）
    k = max(1, min(n, 5))  # 控制数量不要太大，以免运行太慢
    # 随机生成 k 个互不相同的坐标作为已有树
    coords = set()
    while len(coords) < k:
        x = random.randint(1, n)
        y = random.randint(1, m)
        coords.add((x, y))

    pairs = list(coords)

    last_tree = (1, 1)
    maxd = 0
    mult = m * n

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            md = mult
            for x, y in pairs:
                d = abs(i - x) + abs(j - y)
                md = min(md, d)
            if md > maxd:
                last_tree = (i, j)
                maxd = md

    # 模拟原始程序写入 output.txt
    with open("output.txt", "w") as out_file:
        out_file.write(f"{last_tree[0]} {last_tree[1]}")

    # 同时返回结果，便于在函数调用环境中直接使用
    return last_tree


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)