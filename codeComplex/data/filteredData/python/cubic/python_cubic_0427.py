import random

def main(n):
    # 生成测试数据：n 行，m 列，k 为偶数
    m = n  # 这里设为正方形网格，可按需要修改为其他函数，如 m = 2*n
    k = 2 * max(1, n // 2)  # 保证为正且为偶数

    # 随机生成边权（1~9）
    # 水平方向边：n 行，每行 m-1 个权值
    horiz = [[random.randint(1, 9) for _ in range(m - 1)] for _ in range(n)]
    # 垂直方向边：n-1 行，每行 m 个权值
    vert = [[random.randint(1, 9) for _ in range(m)] for _ in range(n - 1)]

    # 原代码逻辑开始（除了 input 改为使用上述测试数据）
    M = [[[] for _ in range(m)] for _ in range(n)]
    S = [[-1] * m for _ in range(n)]

    # 构建水平方向的图
    for y in range(n):
        L = horiz[y]
        for x in range(m - 1):
            M[y][x].append(((y, x + 1), L[x]))
            M[y][x + 1].append(((y, x), L[x]))

    # 构建垂直方向的图
    for y in range(n - 1):
        L = vert[y]
        for x in range(m):
            M[y][x].append(((y + 1, x), L[x]))
            M[y + 1][x].append(((y, x), L[x]))

    if k % 2 == 0:
        for _ in range(k // 2):
            S2 = [[0] * m for _ in range(n)]
            for y in range(n):
                for x in range(m):
                    Mi = 10**30
                    for ((a, b), p) in M[y][x]:
                        Mi = min(Mi, max(0, S[a][b]) + p)
                    S2[y][x] = Mi
            S = S2

        for y in range(n):
            for x in range(m):
                S[y][x] *= 2

    # 输出结果
    for y in range(n):
        print(' '.join(map(str, S[y])))


if __name__ == "__main__":
    # 示例调用：规模 n 可在此处修改
    main(4)