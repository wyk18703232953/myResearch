def check(x, y):
    return ''.join([''.join(s) for s in x]) == ''.join([''.join(s) for s in y])


def generate_board(n):
    # 生成一个 n×n 的随机 '0'/'1' 棋盘
    import random
    return [[random.choice('01') for _ in range(n)] for _ in range(n)]


def main(n):
    import copy

    # 根据 n 生成测试数据
    a = generate_board(n)
    # 复制 a，随后随机做若干次变换，得到 b
    b = copy.deepcopy(a)

    # 随机对 b 进行若干次旋转/翻转，保证有一定概率 Yes，也有概率 No
    import random
    ops = ['none', 'hflip', 'vflip', 'rot']
    for _ in range(random.randint(0, 6)):
        op = random.choice(ops)
        if op == 'hflip':
            b = [row[::-1] for row in b]            # 水平翻转
        elif op == 'vflip':
            b = b[::-1]                             # 垂直翻转
        elif op == 'rot':
            c = [['' for _ in range(n)] for _ in range(n)]
            for t in range(n):
                for u in range(n):
                    c[t][u] = b[u][n - t - 1]       # 顺时针旋转 90°
            b = c

    # 也有一定概率破坏 b，使结果为 No
    if random.random() < 0.5:
        i, j = random.randrange(n), random.randrange(n)
        b[i][j] = '1' if b[i][j] == '0' else '0'

    # 以下为原始逻辑（不使用 input）
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
            b = [s[::-1] for s in b]
        c = [['' for _ in range(n)] for _ in range(n)]
        for t in range(n):
            for u in range(n):
                c[t][u] = b[u][n - t - 1]
        b = c[:]
        if check(a, b):
            print('Yes')
            return
    print('No')