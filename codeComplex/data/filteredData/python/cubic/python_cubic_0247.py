import random


def solve(R, G, B, Rs, Gs, Bs):
    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]
    Rs.sort(reverse=True)
    Gs.sort(reverse=True)
    Bs.sort(reverse=True)
    answer = 0
    for r in range(R + 1):
        for g in range(G + 1):
            for b in range(B + 1):
                if r > 0 and g > 0:
                    dp[r][g][b] = max(dp[r][g][b],
                                      dp[r - 1][g - 1][b] + Rs[r - 1] * Gs[g - 1])
                if g > 0 and b > 0:
                    dp[r][g][b] = max(dp[r][g][b],
                                      dp[r][g - 1][b - 1] + Gs[g - 1] * Bs[b - 1])
                if r > 0 and b > 0:
                    dp[r][g][b] = max(dp[r][g][b],
                                      dp[r - 1][g][b - 1] + Rs[r - 1] * Bs[b - 1])
                answer = max(answer, dp[r][g][b])
    return answer


def main(n):
    # 根据规模 n 生成测试数据：
    # 这里将 R, G, B 设为 n，数值随机取 1..100
    R = G = B = n
    Rs = [random.randint(1, 100) for _ in range(R)]
    Gs = [random.randint(1, 100) for _ in range(G)]
    Bs = [random.randint(1, 100) for _ in range(B)]

    ans = solve(R, G, B, Rs, Gs, Bs)
    print(ans)


if __name__ == '__main__':
    # 示例：使用 n = 5 运行
    main(5)