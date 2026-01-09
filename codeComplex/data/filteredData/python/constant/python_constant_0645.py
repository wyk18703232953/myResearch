def COMMON(WHITE, BLACK):
    x1, y1, x2, y2 = WHITE
    x3, y3, x4, y4 = BLACK
    return (max(x1, x3), max(y1, y3), min(x2, x4), min(y2, y4))


def BtoW(WHITE):
    x1, y1, x2, y2 = WHITE
    if (x1 + y1) % 2 == 0:
        return (x2 - x1 + 1) * (y2 - y1 + 1) // 2

    else:
        return (x2 - x1 + 1) * (y2 - y1 + 1) - (x2 - x1 + 1) * (y2 - y1 + 1) // 2


def WtoB(BLACK):
    x1, y1, x2, y2 = BLACK
    if (x1 + y1) % 2 == 1:
        return (x2 - x1 + 1) * (y2 - y1 + 1) // 2

    else:
        return (x2 - x1 + 1) * (y2 - y1 + 1) - (x2 - x1 + 1) * (y2 - y1 + 1) // 2


def generate_testcase(i, base_n):
    # n, m grow with i and base_n to scale the problem size deterministically
    n = base_n + i
    m = base_n + 2 * i

    # Construct WHITE and BLACK rectangles deterministically
    # Coordinates are 1-based and within grid [1..n] x [1..m]
    x1 = 1 + (i % max(1, n // 3))
    y1 = 1 + (i % max(1, m // 3))
    x2 = min(n, x1 + (i % max(1, n // 2)))
    y2 = min(m, y1 + (i % max(1, m // 2)))
    WHITE = [x1, y1, x2, y2]

    x3 = 1 + ((2 * i + 1) % max(1, n // 2))
    y3 = 1 + ((2 * i + 1) % max(1, m // 2))
    x4 = min(n, x3 + ((3 * i + 1) % max(1, n // 2)))
    y4 = min(m, y3 + ((3 * i + 1) % max(1, m // 2)))
    BLACK = [x3, y3, x4, y4]

    return [n, m], WHITE, BLACK


def main(n):
    # n controls both number of testcases and board sizes
    testcase = max(1, n)
    base_n = max(2, n)

    T = []
    for i in range(testcase):
        nm, WHITE, BLACK = generate_testcase(i, base_n)
        T.extend([nm, WHITE, BLACK])

    for test in range(testcase):
        n_val, m_val = T[test * 3]
        WHITE = T[test * 3 + 1]
        BLACK = T[test * 3 + 2]

        ANSB = n_val * m_val // 2
        ANSW = n_val * m_val - ANSB

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

        # print(ANSW, ANSB)
        pass
if __name__ == "__main__":
    main(10)