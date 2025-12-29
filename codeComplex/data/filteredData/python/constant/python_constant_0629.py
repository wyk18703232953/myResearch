import random

def pre(x, y):
    w = x * (y // 2) + (y % 2) * (x + 1) // 2
    b = x * (y // 2) + (y % 2) * x // 2
    assert w + b == x * y
    return w

def count(x1, y1, x2, y2):
    w = pre(x2, y2) + pre(x1 - 1, y1 - 1) - pre(x2, y1 - 1) - pre(x1 - 1, y2)
    b = (x2 - x1 + 1) * (y2 - y1 + 1) - w
    return w, b

def main(n):
    """
    使用规模参数 n 自动生成测试数据并执行逻辑。
    约定：
      - 测试用例数量 t = n
      - 棋盘大小 n_i, m_i 在 [1, n]
      - 矩形坐标在棋盘范围内随机生成
    """
    random.seed(0)
    t = n
    for _ in range(t):
        # 棋盘大小：1..n
        N = random.randint(1, n)
        M = random.randint(1, n)

        # 随机生成一个合法矩形 [x1, y1] - [x2, y2]
        x1 = random.randint(1, N)
        x2 = random.randint(x1, N)
        y1 = random.randint(1, M)
        y2 = random.randint(y1, M)

        # 再生成另一个合法矩形 [x3, y3] - [x4, y4]
        x3 = random.randint(1, N)
        x4 = random.randint(x3, N)
        y3 = random.randint(1, M)
        y4 = random.randint(y3, M)

        w = pre(M, N)
        b = M * N - w

        # white spill
        wc, bc = count(x1, y1, x2, y2)
        w -= wc
        b -= bc
        w += (x2 - x1 + 1) * (y2 - y1 + 1)

        # black spill
        if max(x1, x3) <= min(x2, x4) and max(y1, y3) <= min(y2, y4):
            x5 = max(x1, x3)
            y5 = max(y1, y3)
            x6 = min(x2, x4)
            y6 = min(y2, y4)
            w -= (x6 - x5 + 1) * (y6 - y5 + 1)
            wc, bc = count(x5, y5, x6, y6)
            w += wc
            b += bc

        wc, bc = count(x3, y3, x4, y4)
        w -= wc
        b -= bc
        b += (x4 - x3 + 1) * (y4 - y3 + 1)

        print(w, b)


if __name__ == "__main__":
    # 示例：使用规模 n = 5 运行
    main(5)