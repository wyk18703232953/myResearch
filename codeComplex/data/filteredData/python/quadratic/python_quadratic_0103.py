def check(x, y):
    return ''.join([''.join(s) for s in x]) == ''.join([''.join(s) for s in y])

def main(n):
    # 生成确定性的 n x n 字符矩阵 a 和 b
    # 使用 'a' 和 'b' 两种字符，以位置 (i + j) 的奇偶性作为构造规则
    a = [['a' if (i + j) % 2 == 0 else 'b' for j in range(n)] for i in range(n)]
    # 将 a 旋转 90 度（与原程序中的变换一致），再作为 b
    b = [['' for _ in range(n)] for _ in range(n)]
    for t in range(n):
        for u in range(n):
            b[t][u] = a[n - u - 1][t]

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
    main(5)