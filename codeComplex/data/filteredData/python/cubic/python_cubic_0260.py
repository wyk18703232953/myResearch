import random

def main(n):
    # 生成规模为 n 的随机测试数据
    # 为了更好地测试 DP，三种颜色数量都设为 n
    R = G = B = n

    # 生成随机非负整数，范围可按需调整
    r = [random.randint(0, 1000) for _ in range(R)]
    g = [random.randint(0, 1000) for _ in range(G)]
    b = [random.randint(0, 1000) for _ in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    # 为安全起见，dp 尺寸依赖于 n，而非固定 205
    # dp[x][y][z]：使用 r 前 x 个、g 前 y 个、b 前 z 个时的最大得分
    # 这里沿用原代码的递归写法和语义，只是将上界改为 R,G,B
    dp = [[[-1 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]

    def recurser(x, y, z):
        # 当任意两种颜色已经全部用完时，无法再配对
        if (x >= R and y >= G) or (y >= G and z >= B) or (z >= B and x >= R):
            return 0
        if dp[x][y][z] != -1:
            return dp[x][y][z]

        maxi = 0
        # 选 r[x] 和 g[y]
        if x < R and y < G:
            maxi = max(maxi, r[x] * g[y] + recurser(x + 1, y + 1, z))
        # 选 g[y] 和 b[z]
        if y < G and z < B:
            maxi = max(maxi, g[y] * b[z] + recurser(x, y + 1, z + 1))
        # 选 r[x] 和 b[z]
        if z < B and x < R:
            maxi = max(maxi, r[x] * b[z] + recurser(x + 1, y, z + 1))

        dp[x][y][z] = maxi
        return maxi

    ans = recurser(0, 0, 0)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(5)