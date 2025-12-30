import random

def solve(mat1: list, mat2: list, K: int) -> list:
    m = len(mat1)
    n = len(mat1[0]) if m > 0 else 0

    if K % 2 == 1:
        res = [[-1] * n for _ in range(m)]
    else:
        # dp[i][j][k] 为从任意地方走到 (i, j) 且只走 k 步的最小无聊数
        half = K // 2
        dp = [[[-1] * (half + 1) for _ in range(n)] for _ in range(m)]
        for k in range(half + 1):
            for i in range(m):
                for j in range(n):
                    if k == 0:
                        dp[i][j][k] = 0
                    else:
                        cur = dp[i][j][k]
                        # 从上方来
                        if i > 0 and dp[i - 1][j][k - 1] != -1:
                            val = dp[i - 1][j][k - 1] + mat2[i - 1][j]
                            if cur == -1 or val < cur:
                                cur = val
                        # 从下方来
                        if i < m - 1 and dp[i + 1][j][k - 1] != -1:
                            val = dp[i + 1][j][k - 1] + mat2[i][j]
                            if cur == -1 or val < cur:
                                cur = val
                        # 从左侧来
                        if j > 0 and dp[i][j - 1][k - 1] != -1:
                            val = dp[i][j - 1][k - 1] + mat1[i][j - 1]
                            if cur == -1 or val < cur:
                                cur = val
                        # 从右侧来
                        if j < n - 1 and dp[i][j + 1][k - 1] != -1:
                            val = dp[i][j + 1][k - 1] + mat1[i][j]
                            if cur == -1 or val < cur:
                                cur = val
                        dp[i][j][k] = cur

        res = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = 2 * dp[i][j][half] if dp[i][j][half] != -1 else -1

    for i in range(m):
        for j in range(n):
            if j < n - 1:
                print(res[i][j], end=' ')
            else:
                print(res[i][j])
    return res


def main(n: int):
    """
    使用规模参数 n 生成测试数据并调用 solve。
    这里约定：
    - 网格大小为 m x n，其中 m = n（也可以按需调整）
    - K 取一个与规模相关的偶数步数，例如 2*n
    - 边权重为 1~10 的随机整数
    """
    m = n
    K = 2 * n  # 需要为偶数才能有非 -1 结果

    random.seed(0)

    # mat1: m 行, 每行 n-1 个数
    if n > 1:
        mat1 = [[random.randint(1, 10) for _ in range(n - 1)] for _ in range(m)]
    else:
        mat1 = [[ ] for _ in range(m)]

    # mat2: m-1 行, 每行 n 个数
    if m > 1:
        mat2 = [[random.randint(1, 10) for _ in range(n)] for _ in range(m - 1)]
    else:
        mat2 = []

    solve(mat1, mat2, K)


if __name__ == "__main__":
    # 示例：使用 n = 4 作为规模
    main(4)