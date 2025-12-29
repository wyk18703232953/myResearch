import random

def main(n):
    # 生成测试数据：
    # n: 行数
    # m: 列数，取一个与 n 同数量级的值
    # k: 可删除的最多人数（1 的个数），不超过总 1 数
    m = max(1, n)  # 简单设定 m = n（至少为 1）

    # 随机生成 0/1 矩阵（a 为字符串列表）
    a = []
    total_ones = 0
    for _ in range(n):
        row_bits = []
        for _ in range(m):
            bit = random.randint(0, 1)
            row_bits.append(str(bit))
            total_ones += bit
        a.append("".join(row_bits))

    # k 不超过总 1 数，且不超过 m
    k = min(total_ones, m)

    # 原逻辑开始
    mem = [[float('inf') if i else 0 for _ in range(k + 1)] for i in range(n + 1)]

    for i in range(n):
        ixs = []
        for j in range(m):
            if a[i][j] == '1':
                ixs.append(j)

        for j in range(k + 1):
            tem = 0
            if j < len(ixs):
                tem, c = float('inf'), 0
                for j1 in range(len(ixs) - j - 1, len(ixs)):
                    tem = min(tem, ixs[j1] - ixs[c] + 1)
                    c += 1

            for j1 in range(k + 1 - j):
                mem[i + 1][j1 + j] = min(mem[i + 1][j1 + j], mem[i][j1] + tem)

    print(mem[n][k])

# 示例运行
if __name__ == "__main__":
    main(5)