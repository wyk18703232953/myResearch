import random

def main(n: int):
    # 1) 根据规模 n 生成 r, g, b
    # 为了让规模和状态数 O(r*g*b) 约为 n，这里简单设 r=g=b≈n**(1/3)
    # 若 n 很小，则至少保证每种颜色非空
    if n <= 0:
        return 0

    side = int(round(n ** (1/3)))
    side = max(side, 1)
    r = g = b = side

    # 2) 生成测试数据：R, G, B 三个数组
    # 生成范围在 [1, 100] 的随机整数并排序
    R = sorted(random.randint(1, 100) for _ in range(r))
    G = sorted(random.randint(1, 100) for _ in range(g))
    B = sorted(random.randint(1, 100) for _ in range(b))

    # 3) 原逻辑封装：三维 DP
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i + j + k < 2:
                    continue
                if i > 0 and j > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j - 1][k] + R[i - 1] * G[j - 1]
                    )
                if i > 0 and k > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j][k - 1] + R[i - 1] * B[k - 1]
                    )
                if j > 0 and k > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i][j - 1][k - 1] + G[j - 1] * B[k - 1]
                    )

    ans = dp[r][g][b]
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：以 n=1000 运行
    main(1000)