import random

def whb(a, b, c, d):
    dim = (c - a + 1) * (d - b + 1)
    col1 = dim // 2
    col2 = dim - col1
    if (a + b) % 2 == 0:
        return [col2, col1]
    else:
        return [col1, col2]

def insegment(a, b, a1, b1):
    li = [[a, 1], [b, 1], [a1, 2], [b1, 2]]
    li.sort()
    if li[0][1] == li[1][1]:
        if li[1][0] == li[2][0]:
            return [li[1][0], li[2][0]]
        else:
            return -1
    else:
        return [li[1][0], li[2][0]]

def inrect(a, b, c, d, a1, b1, c1, d1):
    xra = insegment(a, c, a1, c1)
    yra = insegment(b, d, b1, d1)
    if xra == -1 or yra == -1:
        return -1
    else:
        return [xra[0], yra[0], xra[1], yra[1]]

def main(n):
    """
    n: 测试规模，用作测试数据规模参数。
       这里解释为要生成 n 组测试（q = n）。
       每组测试中棋盘大小在 [1, n]×[1, n] 范围内随机生成，
       两个矩形在棋盘内随机生成且保证坐标有序。
    """
    q = n
    results = []

    for _ in range(q):
        # 随机生成棋盘大小 n_board x m_board
        n_board = random.randint(1, n)
        m_board = random.randint(1, n)

        # 随机生成第一个矩形 (x1,y1) 到 (x2,y2)
        x1 = random.randint(1, n_board)
        x2 = random.randint(x1, n_board)
        y1 = random.randint(1, m_board)
        y2 = random.randint(y1, m_board)

        # 随机生成第二个矩形 (x3,y3) 到 (x4,y4)
        x3 = random.randint(1, n_board)
        x4 = random.randint(x3, n_board)
        y3 = random.randint(1, m_board)
        y4 = random.randint(y3, m_board)

        white, black = whb(1, 1, n_board, m_board)
        w1, b1 = whb(x1, y1, x2, y2)
        w2, b2 = whb(x3, y3, x4, y4)

        black += w2 - b1
        white += b1 - w2

        inter = inrect(x1, y1, x2, y2, x3, y3, x4, y4)
        if isinstance(inter, list):
            w3, b3 = whb(inter[0], inter[1], inter[2], inter[3])
            black += b3
            white -= b3

        # 收集每组的输出
        results.append((white, black))

    # 输出所有结果
    for w, b in results:
        print(w, b)


# 示例：如需直接运行，可取消下面注释
# if __name__ == "__main__":
#     main(5)