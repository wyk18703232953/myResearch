import random

def main(n):
    # n 作为总规模，这里简单地按比例拆成三个长度
    # 确保每个数组至少有 1 个元素
    x = max(1, n // 3)
    y = max(1, n // 3)
    z = max(1, n - x - y)
    sizes = [x, y, z]

    # 生成测试数据：三个数组，元素为 1~100 的随机整数，然后按降序排序
    a = []
    for size in sizes:
        arr = [random.randint(1, 100) for _ in range(size)]
        arr.sort(reverse=True)
        a.append(arr)

    # 原逻辑
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
    # 示例：规模 n = 30
    main(30)