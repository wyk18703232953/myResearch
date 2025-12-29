import random

def main(n: int):
    # 生成规模为 n 的测试数据
    # 这里生成 1 到 3 之间的随机整数，便于形成可合并的段
    arr = [random.randint(1, 3) for _ in range(n)]

    dp = [[-1 for _ in range(n)] for _ in range(n)]

    for size in range(1, n + 1):
        for i in range(n - size + 1):
            j = i + size - 1
            if i == j:
                dp[i][j] = arr[i]
            else:
                for k in range(i, j):
                    if dp[i][k] != -1 and dp[i][k] == dp[k + 1][j]:
                        dp[i][j] = dp[i][k] + 1

    dp2 = [x + 1 for x in range(n)]

    for i in range(n):
        for k in range(i + 1):
            if dp[k][i] != -1:
                if k == 0:
                    dp2[i] = 1
                else:
                    dp2[i] = min(dp2[i], dp2[k - 1] + 1)

    print(dp2[n - 1])


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)