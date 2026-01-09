from collections import defaultdict

def solve2(n, m, x1, y1, x2, y2,
                x3, y3, x4, y4):
    def inside(x, y):
        return 1 <= x <= m and 1 <= y <= n

    def col(a, b):
        assert inside(a, b)
        return 'WB'[(a+b)%2]

    d = {}
    for i in range(1, m+1):
        for j in range(1, n+1):
            d[(i, j)] = col(i, j)
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            d[(i, j)] = 'W'
    for i in range(x3, x4+1):
        for j in range(y3, y4+1):
            d[(i, j)] = 'B'
    return len([P for P in d if d[P] == 'W']), len([P for P in d if d[P] == 'B'])


def solve(n, m, x1, y1, x2, y2,
                x3, y3, x4, y4):

    def inside(x, y):
        return 1 <= x <= m and 1 <= y <= n

    def col(a, b):
        assert inside(a, b)
        return 'WB'[(a+b)%2]

    def cols(x1, y1, x2, y2):
        assert inside(x1, y1) and inside(x2, y2)
        assert x1 <= x2 and y1 <= y2
        w, h = x2+1-x1, y2+1-y1
        if w % 2 == 0 or h % 2 == 0:
            return w*h // 2, w*h // 2

        else:
            WH, BL = w*h // 2, w*h // 2
            if col(x1, y1) == 'W':
                WH += 1

            else:
                BL += 1
            return WH, BL

    def overlap():
        X1 = max(x1, x3)
        X2 = min(x2, x4)
        Y1 = max(y1, y3)
        Y2 = min(y2, y4)
        if X1 > X2 or Y1 > Y2:
            return None
        return X1, Y1, X2, Y2

    tot_wh, tot_bl = cols(1, 1, m, n)
    A_wh, A_bl = cols(x1, y1, x2, y2)
    ovrlp = overlap()
    if ovrlp is not None:
        O_wh, O_bl = cols(*ovrlp)
        assert A_wh >= O_wh and A_bl >= O_bl
        A_wh -= O_wh
        A_bl -= O_bl
    B_wh, B_bl = cols(x3, y3, x4, y4)

    # Paint A white:
    tot_wh += A_bl
    tot_bl -= A_bl

    # Paint B black:
    tot_wh -= B_wh
    tot_bl += B_wh
    return (tot_wh, tot_bl)


def main(n):
    # n 控制测试用例数量和棋盘规模：
    # 第 i 个用例使用棋盘大小 (m, k) = (n + i, n + 2*i)
    # 并生成两个矩形，保证区间合法和有可能重叠
    results = []
    t = max(1, n)
    for i in range(1, t + 1):
        m = n + i          # 行数
        k = n + 2 * i      # 列数

        # 为保证可扩展性，用简单算术构造矩形坐标
        # 第一个矩形 A
        x1 = 1 + (i % m)
        x2 = min(m, x1 + max(1, m // 3))
        y1 = 1 + ((i * 2) % k)
        y2 = min(k, y1 + max(1, k // 4))
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        # 第二个矩形 B
        x3 = 1 + ((i * 3) % m)
        x4 = min(m, x3 + max(1, m // 2))
        y3 = 1 + ((i * 5) % k)
        y4 = min(k, y3 + max(1, k // 3))
        if x3 > x4:
            x3, x4 = x4, x3
        if y3 > y4:
            y3, y4 = y4, y3

        res = solve(k, m, x1, y1, x2, y2, x3, y3, x4, y4)
        results.append(res)

    # 为了在实验脚本中有可见输出，这里打印所有结果
    for wh, bl in results:
        # print(wh, bl)
        pass
if __name__ == "__main__":
    # 示例调用：可在时间复杂度实验中修改 n
    main(5)