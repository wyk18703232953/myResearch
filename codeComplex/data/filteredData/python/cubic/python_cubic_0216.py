import random

def main(n):
    """
    n: int，表示每个数组的规模（原程序中 n[0], n[1], n[2] 都相同）
    该函数内部会随机生成 3 个长度为 n 的数组并执行原逻辑。
    """
    # 三个长度为 n 的数组规模
    sizes = [n, n, n]

    # 生成测试数据：这里用 1~100 的随机整数，可按需要调整
    u = []
    for _ in range(3):
        arr = [random.randint(1, 100) for _ in range(n)]
        u.append(arr)

    # 排序逻辑保持不变：各数组按降序排列
    u[0].sort(reverse=True)
    u[1].sort(reverse=True)
    u[2].sort(reverse=True)

    res = 0
    # 原 dp 规模依赖 n[0], n[1], n[2]
    dp = [[[0] * (sizes[2] + 1) for _ in range(sizes[1] + 1)] for _ in range(sizes[0] + 1)]

    for i in range(sizes[0] + 1):
        for j in range(sizes[1] + 1):
            for k in range(sizes[2] + 1):
                x0 = dp[i - 1][j - 1][k] + u[0][i - 1] * u[1][j - 1] if i and j else 0
                x1 = dp[i][j - 1][k - 1] + u[1][j - 1] * u[2][k - 1] if j and k else 0
                x2 = dp[i - 1][j][k - 1] + u[0][i - 1] * u[2][k - 1] if i and k else 0
                dp[i][j][k] = max(x0, x1, x2)
                res = max(res, dp[i][j][k])

    print(res)
    return res

if __name__ == "__main__":
    # 示例运行：规模为 5，可根据需要修改
    main(5)