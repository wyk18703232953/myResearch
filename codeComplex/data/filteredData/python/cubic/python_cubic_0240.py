import random

def main(n: int):
    # 1. 生成测试数据
    # 将 n 分成 r, g, b 三部分（尽量平均）
    r = n // 3
    g = (n - r) // 2
    b = n - r - g

    # 生成随机正整数作为颜色数组，取值范围可自行调整
    R = [random.randint(1, 1000) for _ in range(r)]
    G = [random.randint(1, 1000) for _ in range(g)]
    B = [random.randint(1, 1000) for _ in range(b)]

    # 2. 原逻辑开始
    R = sorted(R, reverse=True)
    G = sorted(G, reverse=True)
    B = sorted(B, reverse=True)

    # dp[i][j][k]: 取了 i 个红、j 个绿、k 个蓝时的最大得分
    dp = []
    for i in range(r + 1):
        sdp = [[0] * (b + 1) for _ in range(g + 1)]
        dp.append(sdp)

    answer = 0
    for nb_taken in range(r + g + b):
        if nb_taken % 2:
            continue
        for i in range(nb_taken + 1):
            if i > r:
                break
            # j 的下界：nb_taken - i - b
            # j 的上界：nb_taken - i
            for j in range(nb_taken - i - b, nb_taken - i + 1):
                if j < 0:
                    continue
                if j > g:
                    break
                k = nb_taken - i - j
                if k < 0 or k > b:
                    continue
                # 三角不等式相关条件
                if i + j < k or i + k < j or j + k < i:
                    continue

                if i < r and j < g:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        dp[i][j][k] + R[i] * G[j]
                    )
                    answer = max(answer, dp[i + 1][j + 1][k])

                if i < r and k < b:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        dp[i][j][k] + R[i] * B[k]
                    )
                    answer = max(answer, dp[i + 1][j][k + 1])

                if j < g and k < b:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        dp[i][j][k] + G[j] * B[k]
                    )
                    answer = max(answer, dp[i][j + 1][k + 1])

    print(answer)


if __name__ == "__main__":
    # 示例：规模 n = 9
    main(9)