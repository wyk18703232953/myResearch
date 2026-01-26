def quer(x1, y1, x2, y2):
    if x1 > x2 or y1 > y2:
        return [0, 0]
    s = (x2 - (x1 - 1)) * (y2 - (y1 - 1))
    if s % 2 == 0:
        return [s // 2, s // 2]
    if (x1 + y1) & 1:
        return [s // 2 + 1, s // 2]
    return [s // 2, s // 2 + 1]


def main(n):
    q = n
    results = []
    for i in range(q):
        # 生成 n, m
        rows = i + 2
        cols = i + 3

        # 生成第一个矩形 (x1, y1, x2, y2)，在 [1, rows] x [1, cols] 内
        x1 = (i % rows) + 1
        y1 = ((i * 2) % cols) + 1
        x2 = rows
        y2 = cols

        # 生成第二个矩形 (x3, y3, x4, y4)，同样在边界内
        x3 = 1
        y3 = 1
        x4 = max(1, rows - (i % (rows if rows > 0 else 1)))
        y4 = max(1, cols - (i % (cols if cols > 0 else 1)))

        # 计算
        s = quer(1, 1, rows, cols)
        s1 = quer(x1, y1, x2, y2)
        s[0] -= s1[0]
        s[1] += s1[0]

        xmn = max(x1, x3)
        xmx = min(x2, x4)
        ymn = max(y1, y3)
        ymx = min(y2, y4)

        s1 = quer(x3, y3, x4, y4)
        s[0] += s1[1]
        s[1] -= s1[1]
        s1 = quer(xmn, ymn, xmx, ymx)
        s[0] += s1[0]
        s[1] -= s1[0]

        results.append((s[1], s[0]))

    for res in results:
        # print(res[0], res[1])
        pass
if __name__ == "__main__":
    main(10)