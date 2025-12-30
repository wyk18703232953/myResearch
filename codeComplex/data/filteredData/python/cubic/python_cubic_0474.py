d4i = [0, -1, 0, 1]
d4j = [-1, 0, 1, 0]

inf = float('inf')
MOD = 998244353


def makeArr(defaultVal, dimensionArr):  # eg. makeArr(0,[n,m])
    dv = defaultVal
    da = dimensionArr
    if len(da) == 1:
        return [dv for _ in range(da[0])]
    else:
        return [makeArr(dv, da[1:]) for _ in range(da[0])]


def multiLineArrayOfArraysPrint(arr):
    print('\n'.join([' '.join([str(x) for x in y]) for y in arr]))


def main(n):
    """
    n: 规模参数，用于生成测试数据。
       本实现中令:
       - 网格大小: n x n
       - 步数 k:   2 * n
       - 边权：1..10 的简单规则生成
    """
    m = n
    k = 2 * n  # 生成一个与规模相关的偶数步数

    # 生成测试数据: horizontalEdges 和 verticalEdges
    # horizontalEdges[i][j]: i 行 j 列，连接 (i,j) 与 (i,j+1)
    horizontalEdges = []
    for i in range(n):
        row = []
        for j in range(m - 1):
            # 示例生成规则：随 i, j 变化的确定性权重
            row.append((i + j) % 10 + 1)
        horizontalEdges.append(row)

    # verticalEdges[i][j]: i 行 j 列，连接 (i,j) 与 (i+1,j)
    verticalEdges = []
    for i in range(n - 1):
        row = []
        for j in range(m):
            row.append((i * 2 + j * 3) % 10 + 1)
        verticalEdges.append(row)

    if k % 2 == 1:  # 保留原逻辑，虽然这里 k 总是偶数
        ans = makeArr(-1, [n, m])
    else:
        half = k // 2
        dp = makeArr(inf, [n, m, half + 1])  # dp[i][j][moves]

        for i in range(n):
            for j in range(m):
                dp[i][j][0] = 0

        for nM in range(1, half + 1):
            for i in range(n):
                for j in range(m):
                    best = dp[i][j][nM]
                    # move right
                    if j + 1 < m:
                        best = min(best,
                                   dp[i][j + 1][nM - 1] + horizontalEdges[i][j])
                    # move left
                    if j - 1 >= 0:
                        best = min(best,
                                   dp[i][j - 1][nM - 1] + horizontalEdges[i][j - 1])
                    # move down
                    if i + 1 < n:
                        best = min(best,
                                   dp[i + 1][j][nM - 1] + verticalEdges[i][j])
                    # move up
                    if i - 1 >= 0:
                        best = min(best,
                                   dp[i - 1][j][nM - 1] + verticalEdges[i - 1][j])
                    dp[i][j][nM] = best

        ans = makeArr(0, [n, m])
        for i in range(n):
            for j in range(m):
                ans[i][j] = dp[i][j][half] * 2

    multiLineArrayOfArraysPrint(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)