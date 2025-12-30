def main(n):
    # 这里把规模 n 用作正方形网格的边长，同时
    #   m = n（列数）
    #   k = 2 * n（必须为偶数）
    m = n
    k = 2 * n

    # 如果 k 为奇数，按原逻辑输出 -1
    if k % 2 == 1:
        res = [["-1"] * m for _ in range(n)]
        return res

    # 根据 n 生成测试数据：
    # 生成 E_right: n 行，每行 m-1 个权值
    # 生成 E_down : n-1 行，每行 m 个权值
    #
    # 这里示例使用简单的确定性权值，便于测试与复现：
    #   E_right[i][j] = 1 + (i + j) % 9
    #   E_down[i][j]  = 1 + (i * j + i + j) % 9
    E_right = []
    for i in range(n):
        row = []
        for j in range(m - 1):
            row.append(1 + (i + j) % 9)
        # 对于网格右边界，不存在向右的边，填一个占位 0
        row.append(0)
        E_right.append(row)

    E_down = []
    for i in range(n - 1):
        row = []
        for j in range(m):
            row.append(1 + (i * j + i + j) % 9)
        E_down.append(row)

    # DP 部分与原程序一致
    P = [[0 for _ in range(m)] for _ in range(n)]
    new_P = [[0 for _ in range(m)] for _ in range(n)]

    for _step in range(k // 2 + 1):
        for i in range(n):
            for j in range(m):
                possible = []
                if i - 1 >= 0:
                    e = E_down[i - 1][j]
                    possible.append(P[i - 1][j] + e)

                if i + 1 < n:
                    e = E_down[i][j]
                    possible.append(P[i + 1][j] + e)

                if j - 1 >= 0:
                    e = E_right[i][j - 1]
                    possible.append(P[i][j - 1] + e)

                if j + 1 < m:
                    e = E_right[i][j]
                    possible.append(P[i][j + 1] + e)

                new_P[i][j] = min(possible)

        P, new_P = new_P, P

    # 返回结果矩阵（与原程序输出一致：乘以 2）
    result = [[str(s * 2) for s in row] for row in P]
    return result


if __name__ == "__main__":
    # 示例：调用 main(3) 并打印结果
    n = 3
    ans = main(n)
    for row in ans:
        print(" ".join(row))