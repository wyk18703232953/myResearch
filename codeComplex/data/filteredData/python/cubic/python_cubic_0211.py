import random


def main(n: int):
    # 1. 根据规模 n 生成 r, g, b
    #    可按需要调整生成逻辑，这里简单设为 1..n 范围内的随机数
    r = random.randint(1, n)
    g = random.randint(1, n)
    b = random.randint(1, n)

    # 2. 生成三种颜色的棍子长度（1..10^4 随机）
    sticks = []
    for size in (r, g, b):
        arr = [random.randint(1, 10_000) for _ in range(size)]
        arr.sort(reverse=True)
        sticks.append(arr)

    # sticks[0]：红，sticks[1]：绿，sticks[2]：蓝
    dp = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    ans = 0

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                ans = max(ans, dp[i][j][k])
                if i < r and j < g:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        dp[i][j][k] + sticks[0][i] * sticks[1][j],
                    )
                if i < r and k < b:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        dp[i][j][k] + sticks[0][i] * sticks[2][k],
                    )
                if j < g and k < b:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        dp[i][j][k] + sticks[1][j] * sticks[2][k],
                    )

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)