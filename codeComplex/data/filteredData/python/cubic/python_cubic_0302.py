import random

def main(n):
    # 1. 根据规模 n 生成测试数据
    # 为了保持规模一致，令 nr = ng = nb = n
    nr = ng = nb = n

    # 生成随机数组，可以根据需要调整范围
    r = [random.randint(1, 100) for _ in range(nr)]
    g = [random.randint(1, 100) for _ in range(ng)]
    b = [random.randint(1, 100) for _ in range(nb)]

    # 2. 按照原逻辑排序
    r.sort()
    g.sort()
    b.sort()

    # 3. 初始化三维 DP 记忆数组
    memo = [[[ -1 for _ in range(nb + 1)] for __ in range(ng + 1)] for ___ in range(nr + 1)]
    memo[0][0][0] = 0  # i == -1, j == -1, k == -1 时的起点

    for i in range(nr):
        memo[i + 1][0][0] = 0
    for j in range(ng):
        memo[0][j + 1][0] = 0
    for k in range(nb):
        memo[0][0][k + 1] = 0

    # 4. 原递归 dp 函数
    def dp(i, j, k):
        # dp(i,j,k) 是包含 r[i], g[j], b[k] 的最大值
        if i < -1 or j < -1 or k < -1:
            return -float('inf')
        # 由于 i, j, k 可能为 -1, 故在 memo 中偏移 1
        if memo[i + 1][j + 1][k + 1] == -1:
            memo[i + 1][j + 1][k + 1] = max(
                dp(i, j - 1, k - 1) + g[j] * b[k],
                dp(i - 1, j - 1, k) + r[i] * g[j],
                dp(i - 1, j, k - 1) + r[i] * b[k]
            )
        return memo[i + 1][j + 1][k + 1]

    # 5. 计算并返回结果
    return dp(nr - 1, ng - 1, nb - 1)


if __name__ == "__main__":
    # 示例：以 n=3 运行
    result = main(3)
    print(result)