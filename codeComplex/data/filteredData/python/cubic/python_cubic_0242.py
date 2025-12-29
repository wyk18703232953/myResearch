import random

def main(n: int):
    # 规模 n：生成每种颜色的数量
    R = G = B = n

    # 生成测试数据（这里使用 1 到 1000 的随机整数）
    Rs = [random.randint(1, 1000) for _ in range(R)]
    Gs = [random.randint(1, 1000) for _ in range(G)]
    Bs = [random.randint(1, 1000) for _ in range(B)]

    Rs.sort(reverse=True)
    Gs.sort(reverse=True)
    Bs.sort(reverse=True)

    dp = [[[0] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]
    ans = 0

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                t = 0
                if i > 0 and j > 0:
                    v = dp[i - 1][j - 1][k] + Rs[i - 1] * Gs[j - 1]
                    if v > t:
                        t = v
                if j > 0 and k > 0:
                    v = dp[i][j - 1][k - 1] + Gs[j - 1] * Bs[k - 1]
                    if v > t:
                        t = v
                if k > 0 and i > 0:
                    v = dp[i - 1][j][k - 1] + Bs[k - 1] * Rs[i - 1]
                    if v > t:
                        t = v
                dp[i][j][k] = t
                if t > ans:
                    ans = t

    print(ans)


if __name__ == "__main__":
    # 示例：n = 3
    main(3)