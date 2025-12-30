import random

def main(n):
    # 1. 根据规模 n 生成测试数据
    # 为了不让状态空间爆炸，这里让三种颜色数量都为 n
    nr = ng = nb = n

    # 生成随机数据（1~100 的整数）
    r = [random.randint(1, 100) for _ in range(nr)]
    g = [random.randint(1, 100) for _ in range(ng)]
    b = [random.randint(1, 100) for _ in range(nb)]

    # 2. 原逻辑开始
    dp = []
    for _ in range(nr + 1):
        dp.append([[0] * (nb + 1) for _ in range(ng + 1)])

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    mx = 0
    for i in range(nr + 1):
        for j in range(ng + 1):
            for k in range(nb + 1):
                if i and j:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1])
                if i and k:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1])
                if j and k:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1])

    mx_i = mx_j = mx_k = -1

    for i in range(nr + 1):
        for j in range(ng + 1):
            for k in range(nb + 1):
                if dp[i][j][k] > mx:
                    mx_i = i
                    mx_j = j
                    mx_k = k
                    mx = dp[i][j][k]

    print(mx)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)