import random

def main(n):
    """
    n: 规模参数，用来控制三组数组的大小。
       这里示例为将 n 均分到三组 (x, y, z)，可根据需要调整生成规则。
    """
    # 简单的规模分配方案：三组大小尽量接近
    x = n // 3
    y = (n + 1) // 3
    z = n - x - y
    n_list = [x, y, z]

    # 生成测试数据：三组随机正整数
    # 可根据需要修改数值范围
    a = []
    for size in n_list:
        arr = [random.randint(1, 100) for _ in range(size)]
        arr.sort(reverse=True)
        a.append(arr)

    # DP 初始化
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
    # 示例调用：规模 n = 30
    main(30)