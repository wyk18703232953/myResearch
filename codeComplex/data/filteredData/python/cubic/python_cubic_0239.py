import random

def main(n):
    # 这里将 n 用作三个数组的规模上界，并生成随机长度与数据
    # 你也可以按需改写为固定长度 a=b=c=n
    a = random.randint(1, n)
    b = random.randint(1, n)
    c = random.randint(1, n)

    global rs, gs, bs, dp

    # 生成测试数据：值域可根据需要调整
    rs = sorted(random.randint(1, 1000) for _ in range(a))
    gs = sorted(random.randint(1, 1000) for _ in range(b))
    bs = sorted(random.randint(1, 1000) for _ in range(c))

    dp = [[[-1 for _ in range(c + 1)] for _ in range(b + 1)] for _ in range(a + 1)]

    def solve(i, j, k):
        if (i < 0 and j < 0) or (j < 0 and k < 0) or (i < 0 and k < 0):
            return 0
        if dp[i][j][k] != -1:
            return dp[i][j][k]
        ans = 0
        if i >= 0 and j >= 0:
            ans = max(ans, rs[i] * gs[j] + solve(i - 1, j - 1, k))
        if i >= 0 and k >= 0:
            ans = max(ans, rs[i] * bs[k] + solve(i - 1, j, k - 1))
        if j >= 0 and k >= 0:
            ans = max(ans, bs[k] * gs[j] + solve(i, j - 1, k - 1))
        dp[i][j][k] = ans
        return ans

    result = solve(a - 1, b - 1, c - 1)
    print(result)


if __name__ == "__main__":
    # 示例：使用 n=5 作为规模参数
    main(5)