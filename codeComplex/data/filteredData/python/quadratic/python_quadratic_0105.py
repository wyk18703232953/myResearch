import random

def check(x, y):
    return ''.join([''.join(s) for s in x]) == ''.join([''.join(s) for s in y])

def main(n: int):
    # 生成测试数据：n x n 的字符矩阵，只用 '.' 和 '#'
    def rand_grid():
        return [[random.choice(['.', '#']) for _ in range(n)] for _ in range(n)]

    a = rand_grid()
    b = rand_grid()

    for _ in range(4):
        for _ in range(2):
            if check(a, b):
                print('Yes')
                return
            b = b[::-1]  # 上下翻转
        for _ in range(2):
            if check(a, b):
                print('Yes')
                return
            b = [row[::-1] for row in b]  # 左右翻转
        # 旋转 90 度
        c = [['' for _ in range(n)] for _ in range(n)]
        for t in range(n):
            for u in range(n):
                c[t][u] = b[u][n - t - 1]
        b = c[:]
        if check(a, b):
            print('Yes')
            return
    print('No')

if __name__ == "__main__":
    # 示例：运行规模为 4
    main(4)