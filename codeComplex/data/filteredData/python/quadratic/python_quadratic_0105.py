def check(x, y):
    return ''.join([''.join(s) for s in x]) == ''.join([''.join(s) for s in y])

def main(n):
    # n 为矩阵规模 n x n
    # 生成确定性的 a 和 b
    # a 为对角线为 '#' 的矩阵
    a = [['#' if i == j else '.' for j in range(n)] for i in range(n)]
    # b 为 a 旋转 90 度后的结果，再进行一次固定翻转，保证有结构但不完全相同
    # 先生成 a_rot: 旋转 90 度
    a_rot = [['' for _ in range(n)] for _ in range(n)]
    for t in range(n):
        for u in range(n):
            a_rot[t][u] = a[n - u - 1][t]
    # 再将 a_rot 按行反转形成 b
    b = [row[::-1] for row in a_rot]

    for _ in range(4):
        for _ in range(2):
            if check(a, b):
                # print('Yes')
                pass
                return
            b = b[::-1]
        for _ in range(2):
            if check(a, b):
                # print('Yes')
                pass
                return
            b = [s[::-1] for s in b]
        c = [['' for _ in range(n)] for _ in range(n)]
        for t in range(n):
            for u in range(n):
                c[t][u] = b[u][n - t - 1]
        b = c[:]
        if check(a, b):
            # print('Yes')
            pass
            return
    # print('No')
    pass
if __name__ == "__main__":
    main(10)