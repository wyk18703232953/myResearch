import random

def main(n):
    # n 为规模，这里将三类物品数量都设为 n
    n0 = n1 = n2 = n
    sizes = [n0, n1, n2]

    # 生成测试数据：三组长度为 n 的随机正整数
    # 可根据需要调整取值范围
    a = []
    for i in range(3):
        arr = [random.randint(1, 1000) for _ in range(sizes[i])]
        arr.sort(reverse=True)
        a.append(arr)

    dp = [[[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)] for _ in range(n0 + 1)]
    ans = 0

    for i in range(n0 + 1):
        for j in range(n1 + 1):
            for k in range(n2 + 1):
                if i < n0 and j < n1:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        dp[i][j][k] + a[0][i] * a[1][j]
                    )
                if i < n0 and k < n2:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        dp[i][j][k] + a[0][i] * a[2][k]
                    )
                if j < n1 and k < n2:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        dp[i][j][k] + a[1][j] * a[2][k]
                    )
                ans = max(ans, dp[i][j][k])

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 50，可根据需要修改
    main(50)