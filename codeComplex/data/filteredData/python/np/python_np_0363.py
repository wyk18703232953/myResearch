import random

def main(n):
    # n: 问题规模，用来生成测试数据
    # 这里的策略：
    #   c = n（列数）
    #   r = min(n, 8)（行数上限稍微控制，避免 c**r 爆炸）
    #   q = 1（单组测试）
    #
    # 如需不同策略，可自行修改下面的生成方式。

    q = 1
    res = []

    for _ in range(q):
        c = n
        r = min(n, 8)

        # 生成测试矩阵 matt，大小为 c x r
        # 元素范围设为 1..100
        matt = [[random.randint(1, 100) for _ in range(r)] for _ in range(c)]

        # 原始代码逻辑开始
        mat = [[matt[i][j] for i in range(c)] for j in range(r)]
        for i in range(r):
            mat[i].append(max(mat[i]))
            mat[i].reverse()
        mat.sort()
        mat.reverse()
        work = mat[:min(4, r)]
        for t in work:
            t.pop(0)
        r_eff = min(4, r)
        wyn = 0
        for num in range(c ** r_eff):
            shif = [(num // (c ** i)) % c for i in range(r_eff)]
            new = 0
            for i in range(c):
                kol = [work[j][(i + shif[j]) % c] for j in range(r_eff)]
                new += max(kol)
            wyn = max(wyn, new)
        res.append(wyn)

    # 输出所有测试结果
    for v in res:
        print(v)


if __name__ == "__main__":
    # 示例：以 n = 5 运行
    main(5)