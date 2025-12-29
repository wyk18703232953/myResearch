def main(n):
    # 根据规模 n 生成 R,G,B 的数量（均为 n）
    R = G = B = n

    # 生成测试数据：这里简单用从 n 到 1 的递减序列
    Rs = list(range(n, 0, -1))
    Gs = list(range(n, 0, -1))
    Bs = list(range(n, 0, -1))

    # 如果需要可打乱或改成其他生成方式，例如：
    # import random
    # random.shuffle(Rs); random.shuffle(Gs); random.shuffle(Bs)

    # DP 数组
    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]

    # 已经是降序，无需再 sort，如果测试数据生成方式改变，则可保留排序：
    # Rs.sort(reverse=True)
    # Gs.sort(reverse=True)
    # Bs.sort(reverse=True)

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
                if dp[r][g][b] > answer:
                    answer = dp[r][g][b]
    return answer


if __name__ == '__main__':
    # 示例：n = 3
    print(main(3))