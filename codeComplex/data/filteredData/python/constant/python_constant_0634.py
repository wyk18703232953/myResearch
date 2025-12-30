import random

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
    """
    n: 规模参数，用来生成测试数据。
       这里将 n 同时作为网格的尺寸 (n x n) 使用。
       生成 q = n 组随机查询。
    """
    random.seed(0)
    q = n

    for _ in range(q):
        # 生成网格大小 n x n
        N = n
        M = n

        # 生成第一个矩形 [x1, y1, x2, y2]
        x1 = random.randint(1, N)
        x2 = random.randint(x1, N)
        y1 = random.randint(1, M)
        y2 = random.randint(y1, M)

        # 生成第二个矩形 [x3, y3, x4, y4]
        x3 = random.randint(1, N)
        x4 = random.randint(x3, N)
        y3 = random.randint(1, M)
        y4 = random.randint(y3, M)

        # 以下为原逻辑
        s = quer(1, 1, N, M)
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

        print(*s[::-1])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)