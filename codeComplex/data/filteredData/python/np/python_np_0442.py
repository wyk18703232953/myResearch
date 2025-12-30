import random

def main(n, m=None, seed=0):
    random.seed(seed)
    if m is None:
        # 让 m 与 n 同量级，可按需要调整
        m = max(1, min(8, n))  # 保证 m 不超过 8，避免位掩码过大导致 2^m 过大

    # 生成测试数据：矩阵 n x m，元素在 [1, 1e9] 范围内
    l = []
    an = -1
    a = b = 0
    for i in range(n):
        row = [random.randint(1, 10**9) for _ in range(m)]
        l.append(row + [i + 1])  # 原代码在行末添加行号（1-based）
        mn = min(row)
        if an < mn:
            an = mn
            a = b = i + 1

    le = an
    r = 10**9 + 1
    while le < r:
        md = (le + r) // 2
        f = 0
        a1 = a2 = -1
        s = [0] * n

        # 按阈值 md 生成每一行的掩码
        for i in range(n):
            mask = 0
            for j in range(m):
                if l[i][j] >= md:
                    mask |= 1 << j
            s[i] = mask

        po = 1 << m
        d = [0] * po

        # 记录每个掩码最后一次出现的行号（1-based）
        for i in range(n):
            d[s[i]] = i + 1

        # 子集 DP：对每个非空掩码 i，把其所有子掩码的 d 填为 d[i]
        for i in range(1, po):
            if d[i]:
                pp = i
                while pp:
                    d[pp] = d[i]
                    pp = (pp - 1) & i

        # 检查是否存在单行覆盖所有列
        if d[po - 1]:
            f = 1
            a1 = a2 = d[po - 1]

        # 检查两行覆盖所有列
        if not f:
            full = po - 1
            for i in range(1, po):
                if d[i] and d[full ^ i]:
                    f = 1
                    a1 = d[i]
                    a2 = d[full ^ i]
                    break

        if f:
            le = md + 1
            if md > an:
                a, b = a1, a2
                an = md
        else:
            r = md

    print(a, b)


if __name__ == "__main__":
    # 示例：n=5，可按需修改或在外部调用 main(n, m)
    main(5)