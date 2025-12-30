import random

def main(n):
    # 生成测试数据
    # 规模参数 n：行数
    # 这里设定 m 和 k 与 n 相关，可按需要调整
    m = max(1, n // 2)      # 列数
    k = max(0, n // 3)      # 可删除的最多 1 的数量

    # 随机生成 n 行长度为 m 的 0/1 串
    # 保证至少一行有 1，避免原算法中 row[-1] 报错
    grid = []
    has_one = False
    for _ in range(n):
        row = [random.randint(0, 1) for _ in range(m)]
        if any(row):
            has_one = True
        grid.append(row)
    if not has_one:
        # 如若全 0，强制第一行有一个 1
        grid[0][0] = 1

    # 将原逻辑封装
    cls = [
        [i for i, x in enumerate(row) if x]
        for row in grid
    ]

    # 初始化 dp
    dp = [[n * m] * (k + 1) for _ in range(n + 1)]
    dp.append([0] * (k + 1))  # 原代码额外追加一行

    for i in range(n):
        row = cls[i]
        c2l = [m + 1] * (m + 1)
        # 若该行有 1，则删除 0 个 1 的代价为该行最左到最右 1 的宽度
        c2l[0] = row[-1] - row[0] + 1 if row else 0
        # 删除 len(row) 个 1（即全部删掉），代价 0
        c2l[len(row)] = 0

        # 枚举保留的连续 1 段，计算删除数量与代价
        for r in range(len(row)):
            for l in range(r + 1):
                removed = len(row) - (r - l + 1)
                length = row[r] - row[l] + 1
                c2l[removed] = min(c2l[removed], length)

        # 状态转移
        for j in range(k + 1):
            for c, length in enumerate(c2l):
                if j + c <= k and length < m + 1:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j + c] + length)

    ans = min(dp[n - 1])
    # 返回结果以及用于调试的生成数据
    return ans, grid, m, k

# 示例调用
if __name__ == "__main__":
    # 可修改 n 测试不同规模
    result, grid, m, k = main(6)
    print("m =", m, "k =", k)
    print("grid:")
    for row in grid:
        print("".join(map(str, row)))
    print("answer:", result)