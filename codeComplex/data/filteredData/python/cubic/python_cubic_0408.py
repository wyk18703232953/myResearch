import random

def main(n):
    # 生成规模参数
    # n 行，m 列，k 步数
    m = n                      # 示例：令 m = n
    k = 2 * n                  # 示例：令 k 为偶数，方便走到 else 分支

    # 生成测试数据 p, q
    # p: n x m 的非负权值
    # q: (n-1) x m 的非负权值
    # 这里使用 1~10 的随机整数作为权值
    random.seed(0)
    p = [[random.randint(1, 10) for _ in range(m)] for _ in range(n)]
    q = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    def f(g):
        r = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                l = []
                if i - 1 >= 0:
                    l.append(g[i - 1][j] + q[i - 1][j])
                if i + 1 < n:
                    l.append(g[i + 1][j] + q[i][j])
                if j - 1 >= 0:
                    l.append(g[i][j - 1] + p[i][j - 1])
                if j + 1 < m:
                    l.append(g[i][j + 1] + p[i][j])
                r[i][j] = min(l)
        return r

    g = [[0] * m for _ in range(n)]

    if k % 2 != 0:
        for i in range(n):
            for j in range(m):
                g[i][j] = -1
            print(*g[i])
    else:
        for _ in range(k // 2):
            g = f(g)
        for i in range(n):
            for j in range(m):
                g[i][j] *= 2
            print(*g[i])


if __name__ == "__main__":
    # 示例调用：n = 4
    main(4)