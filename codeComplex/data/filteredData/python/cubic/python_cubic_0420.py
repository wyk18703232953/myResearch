import random

INF = int(1e8)


def main(n):
    # 这里将原来的 (n, m) 简化为正方形网格：n 行 n 列
    m = n

    # ========== 1. 生成测试数据 ==========
    # 生成 right 和 down 的边权：
    # right[i][j] 表示从 (i, j) 到 (i, j+1) 的代价，大小随机 [1, 9]
    # down[i][j]  表示从 (i, j) 到 (i+1, j) 的代价，大小随机 [1, 9]
    random.seed(0)
    right = [[random.randint(1, 9) for _ in range(m - 1)] for _ in range(n)]
    down = [[random.randint(1, 9) for _ in range(m)] for _ in range(n - 1)]

    # 这里给一个示例的步数 k，可以按需要改为参数
    k = 4

    def around(r, c):
        a = []
        for i, j in ((r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)):
            if 0 <= i < n and 0 <= j < m:
                a.append((i, j))
        return a

    def solve():
        pdist = [[0] * m for _ in range(n)]
        if k & 1:
            return [[-1] * m for _ in range(n)]
        for _ in range(k // 2):
            dist = [[0] * m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    adist = []
                    for ip, jp in around(i, j):
                        if ip == i:
                            # 水平移动
                            if jp > j:
                                w = right[i][j]
                            else:
                                w = right[i][jp]
                        else:
                            # 垂直移动
                            if ip > i:
                                w = down[i][j]
                            else:
                                w = down[ip][j]
                        adist.append(pdist[ip][jp] + w)
                    dist[i][j] = min(adist)
            pdist = dist
        for i in range(n):
            for j in range(m):
                pdist[i][j] *= 2
        return pdist

    res = solve()
    for row in res:
        print(*row)


if __name__ == "__main__":
    # 示例调用：规模 n=5
    main(5)