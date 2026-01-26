def main(n: int):
    # 生成规模为 n 的测试数据：
    # 让 r, g, b 三种颜色的数量之和为 n，尽量平均分配
    r = n // 3
    g = (n - r) // 2
    b = n - r - g

    # 构造递增的测试数组（也可以换成其他规则，只要是可复现的）
    R = [i + 1 for i in range(r)]
    G = [i + 1 for i in range(g)]
    B = [i + 1 for i in range(b)]

    # 按题意需要是已排序的
    R.sort()
    G.sort()
    B.sort()

    # 动态规划部分与原 solve() 一致，
    # 只是使用生成的 R,G,B 和 r,g,b，而不再从 input 读取
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i + j + k < 2:
                    continue
                if i > 0 and j > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j - 1][k] + R[i - 1] * G[j - 1],
                    )
                if i > 0 and k > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j][k - 1] + R[i - 1] * B[k - 1],
                    )
                if j > 0 and k > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i][j - 1][k - 1] + G[j - 1] * B[k - 1],
                    )
    return dp[r][g][b]


if __name__ == "__main__":
    # 示例：n = 9，可以根据需要修改或由外部调用 main(n)
    result = main(9)
    # print(result)
    pass