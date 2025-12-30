import random


def main(n: int):
    # 1. 生成测试数据
    # 为了让规模可控，这里令三种颜色数组长度都为 n
    nr = ng = nb = n

    # 可以按需要修改生成规则，例如范围、是否允许负数等
    r = [random.randint(1, 10**4) for _ in range(nr)]
    g = [random.randint(1, 10**4) for _ in range(ng)]
    b = [random.randint(1, 10**4) for _ in range(nb)]

    r.sort()
    g.sort()
    b.sort()

    # 2. 原算法逻辑（去除 input，封装到 main 中）
    # memo[i+1][j+1][k+1] 对应原代码中 dp(i,j,k)
    memo = [[[-1 for _ in range(nb + 1)] for __ in range(ng + 1)] for ___ in range(nr + 1)]
    memo[0][0][0] = 0  # starting point when i==-1,j==-1,k==-1

    for i in range(nr):
        memo[i + 1][0][0] = 0
    for j in range(ng):
        memo[0][j + 1][0] = 0
    for k in range(nb):
        memo[0][0][k + 1] = 0

    def dp(i, j, k):  # dp(i,j,k) is the max value including r[i],g[j],b[k]
        if i < -1 or j < -1 or k < -1:
            return -float("inf")
        if memo[i + 1][j + 1][k + 1] == -1:  # offset by 1 because i,j,k can be -1
            memo[i + 1][j + 1][k + 1] = max(
                dp(i, j - 1, k - 1) + g[j] * b[k],
                dp(i - 1, j - 1, k) + r[i] * g[j],
                dp(i - 1, j, k - 1) + r[i] * b[k],
            )
        return memo[i + 1][j + 1][k + 1]

    for i in range(max(nr, ng, nb)):
        dp(min(i, nr - 1), min(i, ng - 1), min(i, nb - 1))

    ans = dp(nr - 1, ng - 1, nb - 1)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)