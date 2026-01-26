def main(n):
    # 映射规模：R, G, B 的大小与 n 挂钩，保持同阶
    # 确保至少为 1，避免 0 尺寸
    R = max(1, n)
    G = max(1, n // 2 if n > 1 else 1)
    B = max(1, n // 3 if n > 2 else 1)

    # 确定性数据生成：简单算术序列，逆序排序后与原逻辑一致
    r = sorted([i * 2 + 1 for i in range(R)], reverse=True)
    g = sorted([i * 3 + 2 for i in range(G)], reverse=True)
    b = sorted([i * 5 + 3 for i in range(B)], reverse=True)

    # 使用闭包捕获 R,G,B,r,g,b
    dpt = [[[-1 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]

    def f(x, y, z):
        m1 = 0
        m2 = 0
        m3 = 0
        if x < R and y < G:
            if dpt[x + 1][y + 1][z] == -1:
                dpt[x + 1][y + 1][z] = f(x + 1, y + 1, z)
            m1 = r[x] * g[y] + dpt[x + 1][y + 1][z]
        if y < G and z < B:
            if dpt[x][y + 1][z + 1] == -1:
                dpt[x][y + 1][z + 1] = f(x, y + 1, z + 1)
            m2 = g[y] * b[z] + dpt[x][y + 1][z + 1]
        if z < B and x < R:
            if dpt[x + 1][y][z + 1] == -1:
                dpt[x + 1][y][z + 1] = f(x + 1, y, z + 1)
            m3 = r[x] * b[z] + dpt[x + 1][y][z + 1]
        dpt[x][y][z] = max(m1, m2, m3)
        return dpt[x][y][z]

    result = f(0, 0, 0)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例：可根据需要修改 n 的大小做复杂度实验
    main(5)