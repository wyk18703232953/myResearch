import random

def main(n):
    # n 为规模，这里用来生成三个长度均为 n 的数组
    # 原题中是三个长度分别为 n[0], n[1], n[2] 的数组，这里统一设为 n
    n_list = [n, n, n]

    # 生成测试数据：三个长度为 n 的整数数组
    # 可根据需要调整数据范围
    a = []
    for _ in range(3):
        arr = [random.randint(1, 100) for _ in range(n)]
        arr.sort(reverse=True)
        a.append(arr)

    dp = [[[0 for _ in range(n_list[2] + 1)]
           for _ in range(n_list[1] + 1)]
          for _ in range(n_list[0] + 1)]

    ans = 0
    for i in range(n_list[0] + 1):
        for j in range(n_list[1] + 1):
            for k in range(n_list[2] + 1):
                if i < n_list[0] and j < n_list[1]:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        dp[i][j][k] + a[0][i] * a[1][j]
                    )
                if i < n_list[0] and k < n_list[2]:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        dp[i][j][k] + a[0][i] * a[2][k]
                    )
                if j < n_list[1] and k < n_list[2]:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        dp[i][j][k] + a[1][j] * a[2][k]
                    )
                ans = max(ans, dp[i][j][k])

    print(ans)


if __name__ == "__main__":
    # 示例调用，规模为 3
    main(3)