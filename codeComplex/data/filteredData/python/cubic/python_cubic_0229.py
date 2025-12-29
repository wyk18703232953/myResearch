import random

def main(n: int):
    # 依据 n 生成 R, G, B 的规模，这里简单设为都等于 n
    R = G = B = n

    # 生成测试数据：随机正整数（可按需修改范围）
    r = sorted([random.randint(1, 100) for _ in range(R)], reverse=True)
    g = sorted([random.randint(1, 100) for _ in range(G)], reverse=True)
    b = sorted([random.randint(1, 100) for _ in range(B)], reverse=True)

    # 3D DP 数组，使用 -1 表示未计算
    dpt = [[[-1 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]

    def f(x, y, z):
        if dpt[x][y][z] != -1:
            return dpt[x][y][z]

        m1 = m2 = m3 = 0

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

    ans = f(0, 0, 0)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)