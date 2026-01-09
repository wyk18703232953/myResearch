def rotate(L):
    n = len(L)
    L1 = ['' for _ in range(n)]
    for i in range(n):
        for j in range(n):
            L1[n - j - 1] += L[i][j]
    return L1

def flip_v(L):
    n = len(L)
    return [L[i][::-1] for i in range(n)]

def flip_h(L):
    n = len(L)
    return [L[n - i - 1] for i in range(n)]

def main(n):
    if n <= 0:
        return
    # 生成确定性 n x n 字符矩阵 L
    # 使用字母表循环生成字符
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    la = len(alphabet)
    L = []
    for i in range(n):
        row = []
        for j in range(n):
            ch = alphabet[(i * n + j) % la]
            row.append(ch)
        L.append("".join(row))

    # 为了保持算法逻辑，在一部分 n 上让 M 等于某个变换结果，其余情况不同
    if n % 4 == 0:
        M = rotate(L)          # 可匹配
    elif n % 4 == 1:
        M = flip_v(L)          # 可匹配
    elif n % 4 == 2:
        M = flip_h(L)          # 可匹配

    else:
        # 构造一个与所有变换都不同的矩阵
        # 将 L 的左上角元素改为不同字符
        first_row = L[0]
        new_char = 'z' if first_row[0] != 'z' else 'y'
        M = L.copy()
        M[0] = new_char + first_row[1:]

    L1 = rotate(L)
    L2 = rotate(L1)
    L3 = rotate(L2)
    L4 = flip_v(L)
    L5 = flip_h(L)
    L6 = rotate(L4)
    L7 = rotate(L6)
    L8 = rotate(L7)
    L9 = rotate(L5)
    L10 = rotate(L9)
    L11 = rotate(L10)

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