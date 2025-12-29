def main(n):
    """
    n 为规模参数，用于生成测试数据：
    这里将 n 拆成三部分 r,g,b 之和，分别为红、绿、蓝数组大小。
    简单策略：r = n//3, g = n//3, b = n - r - g
    数组内容用可重复的递减整数构造，保证有一定的差异性。
    """
    # 1. 生成 r, g, b
    r = n // 3
    g = n // 3
    b = n - r - g

    # 2. 生成测试数据
    # 为了稳定且易于调试，使用确定性构造而非随机：
    # rl, gl, bl 为降序排列
    rl = sorted([10_000 - (i * 3) for i in range(r)], reverse=True)
    gl = sorted([9_000 - (i * 2) for i in range(g)], reverse=True)
    bl = sorted([8_000 - (i * 5) for i in range(b)], reverse=True)

    # 3. 动态规划数组
    dp = [[[-1] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    # 4. 记忆化搜索
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def find(x, y, z):
        ans = 0
        if x < r and y < g:
            ans = max(ans, rl[x] * gl[y] + find(x + 1, y + 1, z))
        if x < r and z < b:
            ans = max(ans, rl[x] * bl[z] + find(x + 1, y, z + 1))
        if y < g and z < b:
            ans = max(ans, gl[y] * bl[z] + find(x, y + 1, z + 1))
        return ans

    # 5. 输出结果
    result = find(0, 0, 0)
    print(result)
    return result


if __name__ == "__main__":
    # 示例：使用规模 n=9 运行一次
    main(9)