def check(x, y):
    return ''.join([''.join(s) for s in x]) == ''.join([''.join(s) for s in y])

def generate_matrix(n):
    # 生成 n×n 的字符矩阵，完全确定性
    # 使用 (i + j) % 2 来决定填充 '1' 或 '0'
    return [[chr(ord('0') + ((i + j) % 2)) for j in range(n)] for i in range(n)]

def main(n):
    # 输入规模 n 表示矩阵的边长
    a = generate_matrix(n)
    b = generate_matrix(n)  # 与 a 相同，使算法必然输出 "Yes"

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
            b = [row[::-1] for row in b]
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
    # 示例调用，可按需修改 n
    main(5)