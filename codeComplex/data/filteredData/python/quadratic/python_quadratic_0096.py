def main(n):
    # n 表示矩阵规模，生成两个 n x n 的字符矩阵
    # ns 为基准矩阵
    ns = []
    for i in range(n):
        row = []
        for j in range(n):
            # 使用简单算术构造一个周期为26的字符序列
            row.append(chr(ord('A') + (i * n + j) % 26))
        ns.append("".join(row))

    # ns2 为 ns 在某种确定性变换下得到的矩阵
    # 为了既保持逻辑，又便于规模实验，这里选用“原样拷贝”：
    # 可以改变下述构造方式，以测试不同情形，但必须保持确定性
    ns2 = []
    for i in range(n):
        ns2.append(ns[i])

    def rotate(i, j):
        return j, n - 1 - i

    def flip(i, j):
        return j, i

    same = True
    for i in range(n):  # 0
        for j in range(n):
            if ns[i][j] != ns2[i][j]:
                same = False
                break
        if same is False:
            break
    if same:
        return True

    same = True
    for i in range(n):  # 1
        for j in range(n):
            a, b = rotate(i, j)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same is False:
            break
    if same:
        return True

    same = True
    for i in range(n):  # 2
        for j in range(n):
            a, b = rotate(i, j)
            a, b = rotate(a, b)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same is False:
            break
    if same:
        return True

    same = True
    for i in range(n):
        for j in range(n):  # 3
            a, b = rotate(i, j)
            a, b = rotate(a, b)
            a, b = rotate(a, b)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same is False:
            break
    if same:
        return True

    same = True
    for i in range(n):  # 0 with flip
        for j in range(n):
            a, b = flip(i, j)
            if ns[a][b] != ns2[i][j]:
                same = False
                break
        if same is False:
            break
    if same:
        return True

    same = True
    for i in range(n):  # 1 with flip
        for j in range(n):
            a, b = rotate(i, j)
            a, b = flip(a, b)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same is False:
            break
    if same:
        return True

    same = True
    for i in range(n):  # 2 with flip
        for j in range(n):
            a, b = rotate(i, j)
            a, b = rotate(a, b)
            a, b = flip(a, b)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same is False:
            break
    if same:
        return True

    same = True
    for i in range(n):  # 3 with flip
        for j in range(n):
            a, b = rotate(i, j)
            a, b = rotate(a, b)
            a, b = rotate(a, b)
            a, b = flip(a, b)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same is False:
            break
    if same:
        return True

    else:
        return False


if __name__ == "__main__":
    # 示例调用：以 n 作为矩阵规模，多次调用应得到确定性结果
    for size in [1, 2, 5, 10]:
        # print(size, main(size))
        pass