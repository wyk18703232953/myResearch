import random

INF = 20000001


class node:
    def __init__(self, l, r, u, d):
        self.u = u
        self.d = d
        self.l = l
        self.r = r
        if l == INF and r == INF and u == INF and d == INF:
            self.marr = [INF for _ in range(11)]
        else:
            self.marr = [0 for _ in range(11)]
            self.marr[1] = min(l, r, u, d)

    def mo(self, st):
        return self.marr[st - 1]


def main(n):
    # 规模参数：n 控制网格大小为 n x n
    # 这里令 m = n，s = 2*n（可根据需要调整）
    m = n
    s = 2 * n

    # 生成测试数据：随机权值 1~9，可根据需要修改
    hor = [[INF for _ in range(m + 3)] for _ in range(n + 2)]
    ver = [[INF for _ in range(m + 2)] for _ in range(n + 3)]

    # 水平边：hor[i][2..m+1]
    for i in range(1, n + 1):
        for j in range(2, m + 2):
            hor[i][j] = random.randint(1, 9)

    # 垂直边：ver[i][1..m], i = 2..n
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            ver[i][j] = random.randint(1, 9)

    if s % 2 == 0:
        nds = [
            [
                node(hor[i][j], hor[i][j + 1], ver[i][j], ver[i + 1][j])
                for j in range(m + 2)
            ]
            for i in range(n + 2)
        ]
        for st in range(2, s // 2 + 1):
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    x = nds[i][j].marr[1]
                    l = nds[i][j].l
                    r = nds[i][j].r
                    u = nds[i][j].u
                    d = nds[i][j].d
                    nds[i][j].marr[st] = min(
                        x * st,
                        r + nds[i][j + 1].mo(st),
                        l + nds[i][j - 1].mo(st),
                        u + nds[i - 1][j].mo(st),
                        d + nds[i + 1][j].mo(st),
                    )
        ans = [[nds[i][j].marr[s // 2] * 2 for j in range(1, m + 1)] for i in range(1, n + 1)]
        for i in range(n):
            print(*tuple(ans[i]))
    else:
        a = [[-1 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            print(*tuple(a[i]))


# 示例：直接调用 main(5) 进行测试
if __name__ == "__main__":
    main(5)