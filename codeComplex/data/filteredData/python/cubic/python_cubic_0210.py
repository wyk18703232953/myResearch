import random

def main(n: int) -> int:
    # 依据规模 n 生成 r, g, b（这里简单设为 n, n, n，可按需调整）
    r = g = b = n

    # 生成测试数据：长度为 r, g, b 的正整数数组
    # 为了更接近原题，一般取 1~10^3 范围即可
    sticks = []
    for _ in range(3):
        arr = [random.randint(1, 1000) for _ in range(n)]
        arr.sort(reverse=True)
        sticks.append(arr)

    # dp[i][j][k] 含义同原代码：使用 i 个红、j 个绿、k 个蓝中的最大价值
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]
    ans = 0

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                cur = dp[i][j][k]
                if i < r and j < g:
                    dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k],
                                              cur + sticks[0][i] * sticks[1][j])
                if i < r and k < b:
                    dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1],
                                              cur + sticks[0][i] * sticks[2][k])
                if j < g and k < b:
                    dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1],
                                              cur + sticks[1][j] * sticks[2][k])
                if cur > ans:
                    ans = cur

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)