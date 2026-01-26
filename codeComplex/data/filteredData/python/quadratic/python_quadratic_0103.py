def check(x, y):
    return ''.join([''.join(s) for s in x]) == ''.join([''.join(s) for s in y])

def generate_matrix(n, offset):
    # 生成 n x n 的字符矩阵，元素为 '0'~'9'，完全由 n 和 offset 确定
    return [[chr(ord('0') + ((i * n + j + offset) % 10)) for j in range(n)] for i in range(n)]

def main(n):
    if n <= 0:
        return
    # 生成两个 n x n 的矩阵 a 和 b
    # a 从 offset=0 开始生成
    a = generate_matrix(n, 0)
    # b 从 offset=n 开始生成，使其通常不同于 a，但确定性可复现
    b = generate_matrix(n, n)

    for i in range(4):
        for j in range(2):
            if check(a, b):
                # print('Yes')
                pass
                return
            b = b[::-1]
        for j in range(2):
            if check(a, b):
                # print('Yes')
                pass
                return
            b = [s[::-1] for s in b]
        c = [['' for t in range(n)] for u in range(n)]
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
    # 示例：使用固定的 n 进行一次调用，保证可重复实验
    main(5)