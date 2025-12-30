import random


def main(n: int):
    """
    n: 问题规模，用于生成测试数据
    逻辑：原程序中 N 行、M 列的矩阵 X
    这里简单设置 N = M = n，并随机生成 X 中的元素
    """
    # 生成测试数据
    N = n
    M = n
    # 随机生成 [0, 100] 的整数矩阵 X
    X = [[random.randint(0, 100) for _ in range(M)] for _ in range(N)]

    # 原逻辑开始
    Y = [[X[i][j] for i in range(N)] for j in range(M)]
    ma = 0
    for _ in range(99):
        for i in range(M):
            a = random.randrange(N)
            Y[i] = [Y[i][j - a] for j in range(N)]
        ma = max(ma, sum([max([Y[i][j] for i in range(M)]) for j in range(N)]))

    # 输出结果
    print(ma)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)