import random

def main(n):
    # 规模 n 用作行数，列数和步数也从 n 派生
    row = n
    col = n
    k = 2 * n  # 保证 k 为偶数，且与规模相关

    # 生成测试数据：right 为 n x (m-1)，down 为 (n-1) x m
    INF_EDGE = 10**6
    right = [[random.randint(1, INF_EDGE) for _ in range(col - 1)] for _ in range(row)]
    down = [[random.randint(1, INF_EDGE) for _ in range(col)] for _ in range(row - 1)]

    # 若 k 为奇数，输出全 -1（此处 k 被设置为偶数，分支保留逻辑完整性）
    if k % 2 == 1:
        for _ in range(row):
            print(" ".join(["-1"] * col))
        return

    half_k = k // 2
    INF = 10**15

    # dp[steps][i][j]：从 (i,j) 出发走 steps 步到任意点的最小代价
    dp = [[[INF] * col for _ in range(row)] for _ in range(half_k + 1)]

    for steps in range(half_k + 1):
        for i in range(row):
            for j in range(col):
                if steps == 0:
                    dp[steps][i][j] = 0
                    continue

                best = INF
                if i > 0:
                    best = min(best, dp[steps - 1][i - 1][j] + down[i - 1][j])
                if i < row - 1:
                    best = min(best, dp[steps - 1][i + 1][j] + down[i][j])
                if j < col - 1:
                    best = min(best, dp[steps - 1][i][j + 1] + right[i][j])
                if j > 0:
                    best = min(best, dp[steps - 1][i][j - 1] + right[i][j - 1])

                dp[steps][i][j] = best

    # 输出结果：走 k (即 2 * half_k) 步回到原点的最小代价
    for i in range(row):
        row_ans = [str(2 * dp[half_k][i][j]) for j in range(col)]
        print(" ".join(row_ans))


if __name__ == "__main__":
    # 示例运行，可修改 n 测试不同规模
    main(5)