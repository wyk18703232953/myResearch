import random

def main(n):
    # n 为规模，这里用来生成三个长度之和为 n 的数组
    # 你可以根据需要修改分配策略
    n0 = n // 3
    n1 = (n - n0) // 2
    n2 = n - n0 - n1
    sizes = [n0, n1, n2]

    # 生成测试数据：三个数组，元素为 1~100 的随机整数
    a = []
    for length in sizes:
        arr = [random.randint(1, 100) for _ in range(length)]
        arr.sort(reverse=True)
        a.append(arr)

    # DP 逻辑与原程序一致
    dp = [[[0 for _ in range(sizes[2] + 1)]
           for _ in range(sizes[1] + 1)]
          for _ in range(sizes[0] + 1)]

    ans = 0
    for i in range(sizes[0] + 1):
        for j in range(sizes[1] + 1):
            for k in range(sizes[2] + 1):
                if i < sizes[0] and j < sizes[1]:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        dp[i][j][k] + a[0][i] * a[1][j]
                    )
                if i < sizes[0] and k < sizes[2]:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        dp[i][j][k] + a[0][i] * a[2][k]
                    )
                if j < sizes[1] and k < sizes[2]:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        dp[i][j][k] + a[1][j] * a[2][k]
                    )
                ans = max(ans, dp[i][j][k])

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 9（将被分配为三段）
    main(9)