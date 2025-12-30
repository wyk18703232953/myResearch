import random

def check(x, y):
    return ''.join([''.join(s) for s in x]) == ''.join([''.join(s) for s in y])

def main(n: int):
    # 生成规模为 n 的随机测试数据矩阵 a、b
    # 使用 '#' 和 '.' 组成的字符矩阵
    chars = ['#', '.']
    a = [[random.choice(chars) for _ in range(n)] for _ in range(n)]
    b = [[random.choice(chars) for _ in range(n)] for _ in range(n)]

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
    # 示例：调用 main(4)
    main(4)