def main(n):
    """
    n 为规模，用于生成测试数据。
    这里用 n 控制每种颜色数组长度：
        r = g = b = n
        rl, gl, bl 为从 n 到 1 的降序数组（可按需修改生成规则）。
    返回计算结果（不打印）。
    """
    # 1. 生成测试数据
    r = g = b = n
    # 示例：生成降序数组 [n, n-1, ..., 1]
    rl = list(range(n, 0, -1))
    gl = list(range(n, 0, -1))
    bl = list(range(n, 0, -1))

    # 2. DP 表
    dp_table = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    # 3. 递归 + 记忆化
    def solve(i, j, k):
        if dp_table[i][j][k] != -1:
            return dp_table[i][j][k]

        ans = 0

        if i < r and j < g:
            ans = max(ans, solve(i + 1, j + 1, k) + rl[i] * gl[j])

        if i < r and k < b:
            ans = max(ans, solve(i + 1, j, k + 1) + rl[i] * bl[k])

        if j < g and k < b:
            ans = max(ans, solve(i, j + 1, k + 1) + gl[j] * bl[k])

        dp_table[i][j][k] = ans
        return ans

    return solve(0, 0, 0)


# 示例: 直接运行本文件时测试
if __name__ == "__main__":
    # 例如用 n = 3 做一组测试
    result = main(3)
    print(result)