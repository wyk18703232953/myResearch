def main(n: int):
    import random

    # 1. 生成测试数据
    # 这里按原程序含义，n 为行数，列数 m 取一个相对小的常数（例如 5）
    m = 5
    # 随机生成一个 n x m 的矩阵，元素范围 [0, 10^9]
    a = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    # 2. 原始逻辑（去掉 input()，改用生成的 a 和 n, m）
    l, r = -1, 10**9 + 1
    ans1, ans2 = -1, -1

    while r - l > 1:
        x = (l + r) // 2
        idx = {}
        for i in range(n):
            v = 0
            for j in range(m):
                if a[i][j] >= x:
                    v += 1
                v <<= 1
            idx[v >> 1] = i

        ok = False
        idx1, idx2 = 0, 0
        full_mask = (1 << m) - 1

        for aa, bb in idx.items():
            for cc, dd in idx.items():
                # 原代码在这里还有一个对 d in range(m) 的循环，但循环体只检查 (aa|cc)，
                # 与 d 无关，因此等价于只检查一次即可。
                if (aa | cc) == full_mask:
                    ok = True
                    idx1 = bb + 1
                    idx2 = dd + 1
                    break
            if ok:
                break

        if ok:
            l = x
            ans1 = idx1
            ans2 = idx2
        else:
            r = x

    print(ans1, ans2)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模（行数）
    main(10)