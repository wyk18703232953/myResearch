import random

def cal(r, g, b, dp, R, G, B, nr, ng, nb):
    if dp[r][g][b] != -1:
        return dp[r][g][b]
    best = 0
    if r < nr and g < ng:
        best = max(best, cal(r + 1, g + 1, b, dp, R, G, B, nr, ng, nb) + R[r] * G[g])
    if r < nr and b < nb:
        best = max(best, cal(r + 1, g, b + 1, dp, R, G, B, nr, ng, nb) + R[r] * B[b])
    if g < ng and b < nb:
        best = max(best, cal(r, g + 1, b + 1, dp, R, G, B, nr, ng, nb) + B[b] * G[g])
    dp[r][g][b] = best
    return dp[r][g][b]

def main(n):
    """
    n: 控制规模的参数（最大颜色数量）；实际数量在 [1, n] 随机生成
    """
    # 生成测试数据规模
    nr = random.randint(1, n)
    ng = random.randint(1, n)
    nb = random.randint(1, n)

    # 生成颜色数组，元素值也可随 n 调整
    R = [random.randint(1, 1000) for _ in range(nr)]
    G = [random.randint(1, 1000) for _ in range(ng)]
    B = [random.randint(1, 1000) for _ in range(nb)]

    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)

    # dp 需要大小为 (nr+1) x (ng+1) x (nb+1)
    dp = [[[-1 for _ in range(nb + 1)] for _ in range(ng + 1)] for _ in range(nr + 1)]

    ans = cal(0, 0, 0, dp, R, G, B, nr, ng, nb)
    print(ans)

if __name__ == '__main__':
    # 示例：n 控制最大数组长度
    main(50)