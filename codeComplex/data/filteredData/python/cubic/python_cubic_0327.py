def cal(r, g, b, R, G, B, rl, gl, bl, dp):
    if dp[r][g][b] != -1:
        return dp[r][g][b]

    area = 0
    if r < R and g < G:
        area = max(area, rl[r] * gl[g] + cal(r + 1, g + 1, b, R, G, B, rl, gl, bl, dp))
    if r < R and b < B:
        area = max(area, rl[r] * bl[b] + cal(r + 1, g, b + 1, R, G, B, rl, gl, bl, dp))
    if g < G and b < B:
        area = max(area, gl[g] * bl[b] + cal(r, g + 1, b + 1, R, G, B, rl, gl, bl, dp))

    dp[r][g][b] = area
    return area


def main(n):
    """
    n: 规模参数，用来生成测试数据。
       这里设定 R = G = B = n，并生成简单的递减序列作为测试数据。
    """
    R = G = B = n

    # 根据 n 生成测试数据，这里使用简单的递减序列：
    # rl = [n, n-1, ..., 1]，gl, bl 同理
    rl = list(range(n, 0, -1))
    gl = list(range(n, 0, -1))
    bl = list(range(n, 0, -1))

    # 确保排序为降序（与原代码一致）
    rl.sort(reverse=True)
    gl.sort(reverse=True)
    bl.sort(reverse=True)

    dp = [[[-1] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]
    result = cal(0, 0, 0, R, G, B, rl, gl, bl, dp)
    print(result)


if __name__ == "__main__":
    # 示例：使用 n = 3 运行
    main(3)