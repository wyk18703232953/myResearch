def check(x, y):
    # 比较两个二维字符数组展开后的字符串是否相等
    return ''.join(''.join(row) for row in x) == ''.join(''.join(row) for row in y)


def generate_test_data(n):
    # 生成一个 n x n 的随机 0/1 矩阵作为 a
    # 再对 a 做若干次变换（旋转、翻转），得到 b
    import random

    a = [[random.choice(['0', '1']) for _ in range(n)] for _ in range(n)]
    b = [row[:] for row in a]

    # 随机选择一些操作作用于 b
    def rotate(mat):
        m = len(mat)
        res = [['' for _ in range(m)] for _ in range(m)]
        for t in range(m):
            for u in range(m):
                res[t][u] = mat[u][m - t - 1]
        return res

    for _ in range(random.randint(0, 4)):
        op = random.choice(['none', 'rev_rows', 'rev_cols', 'rotate'])
        if op == 'rev_rows':
            b = b[::-1]
        elif op == 'rev_cols':
            b = [row[::-1] for row in b]
        elif op == 'rotate':
            b = rotate(b)
        # 'none' 不做处理

    return a, b


def main(n):
    # 生成测试数据
    a, b = generate_test_data(n)
    re = n

    # 原始逻辑
    for _ in range(4):
        for _ in range(2):
            if check(a, b):
                print('Yes')
                return
            b = b[::-1]
        for _ in range(2):
            if check(a, b):
                print('Yes')
                return
            b = [row[::-1] for row in b]
        c = [['' for _ in range(re)] for _ in range(re)]
        for t in range(re):
            for u in range(re):
                c[t][u] = b[u][re - t - 1]
        b = c[:]
        if check(a, b):
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    # 示例：规模为 4
    main(4)