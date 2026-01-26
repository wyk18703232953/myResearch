def rotate(L, n):
    L1 = ['' for _ in range(n)]
    for i in range(n):
        for j in range(n):
            L1[n - j - 1] += L[i][j]
    return L1

def flip_v(L, n):
    L1 = []
    for i in range(n):
        L1.append(L[i][::-1])
    return L1

def flip_h(L, n):
    L1 = []
    for i in range(n):
        L1.append(L[n - i - 1])
    return L1

def main(n):
    if n <= 0:
        return
    # 生成确定性的 n×n 字符矩阵 L 和 M
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    L = []
    M = []
    for i in range(n):
        row_chars = []
        for j in range(n):
            row_chars.append(alphabet[(i * n + j) % len(alphabet)])
        L.append("".join(row_chars))
    for i in range(n):
        row_chars = []
        for j in range(n):
            row_chars.append(alphabet[(i * n + j + 1) % len(alphabet)])
        M.append("".join(row_chars))

    L1 = rotate(L, n)
    L2 = rotate(L1, n)
    L3 = rotate(L2, n)
    L4 = flip_v(L, n)
    L5 = flip_h(L, n)
    L6 = rotate(L4, n)
    L7 = rotate(L6, n)
    L8 = rotate(L7, n)
    L9 = rotate(L5, n)
    L10 = rotate(L9, n)
    L11 = rotate(L10, n)

    if (L == M or L1 == M or L2 == M or L3 == M or
        L4 == M or L5 == M or L6 == M or L7 == M or
        L8 == M or L9 == M or L10 == M or L11 == M):
        # print('Yes')
        pass

    else:
        # print('No')
        pass
if __name__ == "__main__":
    main(5)