import random

def COMMON(WHITE, BLACK):
    x1, y1, x2, y2 = WHITE
    x3, y3, x4, y4 = BLACK
    return (max(x1, x3), max(y1, y3), min(x2, x4), min(y2, y4))

def BtoW(WHITE):
    x1, y1, x2, y2 = WHITE
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    if (x1 + y1) % 2 == 0:
        return area // 2
    else:
        return area - area // 2

def WtoB(BLACK):
    x1, y1, x2, y2 = BLACK
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    if (x1 + y1) % 2 == 1:
        return area // 2
    else:
        return area - area // 2

def main(n):
    """
    n: 规模，用作棋盘最大边长和测试用例数量的上界。
       实际生成 testcase = max(1, n // 3) 组测试。
    """
    random.seed(0)
    testcase = max(1, n // 3)
    tests = []

    for _ in range(testcase):
        # 棋盘尺寸 1..n
        rows = random.randint(1, max(1, n))
        cols = random.randint(1, max(1, n))

        def rand_rect(max_x, max_y):
            x1 = random.randint(1, max_x)
            x2 = random.randint(x1, max_x)
            y1 = random.randint(1, max_y)
            y2 = random.randint(y1, max_y)
            return [x1, y1, x2, y2]

        WHITE = rand_rect(rows, cols)
        BLACK = rand_rect(rows, cols)
        tests.extend([[rows, cols], WHITE, BLACK])

    # 逻辑与原程序一致
    idx = 0
    for _ in range(testcase):
        n_board, m_board = tests[idx]
        WHITE = tests[idx + 1]
        BLACK = tests[idx + 2]
        idx += 3

        ANSB = n_board * m_board // 2
        ANSW = n_board * m_board - ANSB

        WHITE2 = COMMON(WHITE, BLACK)

        k = BtoW(WHITE)
        ANSB -= k
        ANSW += k

        if not (WHITE2[0] > WHITE2[2] or WHITE2[1] > WHITE2[3]):
            l = BtoW(WHITE2)
            ANSB += l
            ANSW -= l

        m = WtoB(BLACK)
        ANSB += m
        ANSW -= m

        print(ANSW, ANSB)

if __name__ == "__main__":
    # 示例：n=10
    main(10)