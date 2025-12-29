import random

def main(n):
    # 生成测试数据：
    # 将 n 拆成三个非负数 r, g, b，使 r + g + b = n
    # 这里简单取三等分（最后一个补齐）
    r = n // 3
    g = n // 3
    b = n - r - g

    # 生成随机测试数据（1~100 的整数）
    ra = sorted([random.randint(1, 100) for _ in range(r)], reverse=True)
    ga = sorted([random.randint(1, 100) for _ in range(g)], reverse=True)
    ba = sorted([random.randint(1, 100) for _ in range(b)], reverse=True)

    # 创建 DP 数组
    dp = [[[-1] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    def solve(i, j, k):
        if dp[i][j][k] != -1:
            return dp[i][j][k]

        if i == r:
            if j == g or k == b:
                return 0
            dp[i][j][k] = ga[j] * ba[k] + solve(i, j + 1, k + 1)

        elif j == g:
            if i == r or k == b:
                return 0
            dp[i][j][k] = ra[i] * ba[k] + solve(i + 1, j, k + 1)

        elif k == b:
            if j == g or i == r:
                return 0
            dp[i][j][k] = ga[j] * ra[i] + solve(i + 1, j + 1, k)

        else:
            dp[i][j][k] = max(
                ra[i] * ga[j] + solve(i + 1, j + 1, k),
                ra[i] * ba[k] + solve(i + 1, j, k + 1),
                ba[k] * ga[j] + solve(i, j + 1, k + 1),
            )

        return dp[i][j][k]

    ans = solve(0, 0, 0)
    print(ans)
    return ans

# 示例调用：
# main(9)