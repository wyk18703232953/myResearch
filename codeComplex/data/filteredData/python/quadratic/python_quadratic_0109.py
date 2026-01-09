def main(n):
    if n <= 0:
        return

    global map1, map2

    # 确定性生成 n x n 的字符矩阵
    # 使用字母和数字循环生成
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    m = len(chars)

    # 生成 map1
    map1 = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(chars[(i * n + j) % m])
        map1.append(row)

    # 生成 map2 为在 map1 上进行 k 次 90 度旋转后的结果
    # 为了让有时匹配、有时不匹配，可根据 n 的奇偶性决定旋转次数
    def rotate_matrix(mat):
        wk = []
        size = len(mat)
        for i in range(size):
            wk.append([])
            for j in range(size):
                wk[i].append(mat[i][j])
        res = [[None] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                res[i][j] = wk[j][size - 1 - i]
        return res

    k_rot = n % 4  # 0~3 次旋转，确定性依赖于 n
    map2 = map1
    for _ in range(k_rot):
        map2 = rotate_matrix(map2)

    # 定义 check 和 rotate，保持原始逻辑
    def check():
        f = True
        for i in range(n):
            for j in range(n):
                if map1[i][j] != map2[i][j]:
                    f = False
                    break
        if f:
            return True

        f = True
        for i in range(n):
            for j in range(n):
                if map1[i][j] != map2[n - 1 - i][j]:
                    f = False
                    break
        if f:
            return True

        f = True
        for i in range(n):
            for j in range(n):
                if map1[i][j] != map2[i][n - 1 - j]:
                    f = False
                    break
        if f:
            return True

    def rotate():
        wk1 = []
        for i in range(n):
            wk1.append([])
            for j in range(n):
                wk1[i].append(map1[i][j])
        for i in range(n):
            for j in range(n):
                map1[i][j] = wk1[j][n - 1 - i]

    f = False
    for _ in range(4):
        if check():
            f = True
            break
        rotate()

    if f:
        # print("Yes")
        pass

    else:
        # print("No")
        pass
if __name__ == "__main__":
    main(5)