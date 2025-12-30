import math
import random


def main(n: int):
    # 生成规模参数
    # 这里假设 m 与 n 相同，k 为偶数，且与 n 成比例
    m = n
    # 确保 k 为偶数（与原题逻辑一致）
    k = 2 * max(1, n // 2)

    # 生成测试数据：right 为 n 行，每行 m-1 个数；down 为 n-1 行，每行 m 个数
    # 使用 1~10 的随机权值
    random.seed(0)
    right = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    down = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    # 处理逻辑
    if k % 2 == 1:
        # 若 k 为奇数，则全为 -1
        for _ in range(n):
            print(" ".join(["-1" for _ in range(m)]))
        return

    dp = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(1, (k // 2) + 1):
        tmp = [[math.inf for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i:
                    tmp[i][j] = min(tmp[i][j], dp[i - 1][j] + 2 * down[i - 1][j])
                if i < n - 1:
                    tmp[i][j] = min(tmp[i][j], dp[i + 1][j] + 2 * down[i][j])
                if j:
                    tmp[i][j] = min(tmp[i][j], dp[i][j - 1] + 2 * right[i][j - 1])
                if j < m - 1:
                    tmp[i][j] = min(tmp[i][j], dp[i][j + 1] + 2 * right[i][j])
        dp = tmp

    for i in range(n):
        print(" ".join(str(x) for x in dp[i]))


# 示例调用
if __name__ == "__main__":
    main(4)