def main(n):
    # 映射规则：n 作为矩阵规模，n x n
    m = n
    if n < 3:
        # 构造一个全 '.' 的矩阵，保持逻辑完整
        u = [['.'] * m for _ in range(n)]

    else:
        # 构造一个确定性的 n x n 字符矩阵
        # 通过 (i + j) % 5 决定字符：其中部分位置为 '#'
        u = []
        for i in range(n):
            row = []
            for j in range(m):
                # 周期性分布 '#'，确保有一定概率出现匹配形状
                if (i + j) % 5 in (0, 1):
                    row.append('#')

                else:
                    row.append('.')
            u.append(row)

    u1 = [['.'] * m for _ in range(n)]

    for i in range(n - 2):
        for j in range(m - 2):
            ok = True
            for k in range(3):
                if u[i][j + k] != '#' or u[i + k][j] != '#':
                    ok = False
                    break
            if ok:
                if (
                    u[i + 2][j + 1] != '#'
                    or u[i + 2][j + 2] != '#'
                    or u[i + 1][j + 2] != '#'
                ):
                    ok = False

                else:
                    for k in range(3):
                        u1[i][j + k] = '#'
                        u1[i + k][j] = '#'
                    u1[i + 2][j + 1] = '#'
                    u1[i + 2][j + 2] = '#'
                    u1[i + 1][j + 2] = '#'

    ok = True
    for i in range(n):
        for j in range(m):
            if u[i][j] != u1[i][j]:
                ok = False
                break
        if not ok:
            break

    if ok:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的大小做规模实验
    main(10)