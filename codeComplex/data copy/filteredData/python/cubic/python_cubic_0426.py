def main(n):
    # 生成测试数据
    # 这里假设：m = n，k = 2 * n，并生成随机或固定的边权
    # 若需修改规模关系或生成方式，可自行调整此部分
    m = n
    k = 2 * n

    # 为了结果可复现，这里用简单的固定模式生成权值：
    # H: n 行，每行 m-1 个数；V: n-1 行，每行 m 个数
    H = [[(i + j) % 9 + 1 for j in range(m - 1)] for i in range(n)]
    V = [[(i * j) % 9 + 1 for j in range(m)] for i in range(n - 1)]

    # 以下为原始逻辑（移除输入封装成函数）

    if k & 1:
        # k 为奇数时，无解，输出全 -1
        res = '\n'.join(' '.join(['-1'] * m) for _ in range(n))
        # print(res)
        pass
        return

    d = [0] * (n * m)
    for _ in range(k // 2):
        nd = [0] * (n * m)
        for x in range(n):
            for y in range(m):
                v = x * m + y
                w = []
                if x:
                    w.append(d[v - m] + V[x - 1][y])
                if y:
                    w.append(d[v - 1] + H[x][y - 1])
                if x < n - 1:
                    w.append(d[v + m] + V[x][y])
                if y < m - 1:
                    w.append(d[v + 1] + H[x][y])
                nd[v] = min(w)
        d = nd

    # 输出结果
    for i in range(n):
        row = d[i * m:i * m + m]
        # print(' '.join(str(2 * x) for x in row))
        pass


# 示例调用（实际使用时按需调用 main）
if __name__ == "__main__":
    main(4)