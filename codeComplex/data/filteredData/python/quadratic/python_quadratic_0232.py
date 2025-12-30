class SegTree:
    def __init__(self, init_val, ide_ele, segfunc):
        self.n = len(init_val)
        self.num = 2 ** (self.n - 1).bit_length()
        self.ide_ele = ide_ele
        self.segfunc = segfunc
        self.seg = [ide_ele] * (2 * self.num)
        # set initial values
        for i in range(self.n):
            self.seg[i + self.num] = init_val[i]
        # build tree
        for i in range(self.num - 1, 0, -1):
            self.seg[i] = self.segfunc(self.seg[2 * i], self.seg[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.seg[k] = x
        while k:
            k >>= 1
            self.seg[k] = self.segfunc(self.seg[2 * k], self.seg[2 * k + 1])

    def query(self, l, r):
        if r <= l:
            return self.ide_ele
        l += self.num
        r += self.num
        lres = self.ide_ele
        rres = self.ide_ele
        while l < r:
            if r & 1:
                r -= 1
                rres = self.segfunc(self.seg[r], rres)
            if l & 1:
                lres = self.segfunc(lres, self.seg[l])
                l += 1
            l >>= 1
            r >>= 1
        return self.segfunc(lres, rres)

    def __str__(self):
        arr = [self.query(i, i + 1) for i in range(self.n)]
        return str(arr)


def main(n):
    # 根据 n 生成测试数据：
    # 这里简单构造：
    #   S 为 0..n-1 的递增序列
    #   C 为 1..n 的递增费用
    # 你可以按需要替换为其他生成逻辑
    if n < 3:
        # 原逻辑在 n < 3 时不会找到 i in [1, n-2]，结果应为 -1
        print(-1)
        return

    S = list(range(n))
    C = list(range(1, n + 1))

    SA = sorted(set(S))
    d = {s: i for i, s in enumerate(SA)}
    S = [d[s] for s in S]

    L = [0] * n
    R = [0] * n
    INF = 10 ** 18
    N = len(d)

    seg = SegTree([INF] * (N + 1), INF, min)
    seg.update(S[0], C[0])
    for i in range(1, n - 1):
        s = S[i]
        L[i] = seg.query(0, s)
        seg.update(s, C[i])

    seg = SegTree([INF] * (N + 1), INF, min)
    seg.update(S[-1], C[-1])
    for i in reversed(range(1, n - 1)):
        s = S[i]
        R[i] = seg.query(s + 1, seg.n)
        seg.update(s, C[i])

    ans = INF
    for i in range(1, n - 1):
        ans = min(ans, L[i] + C[i] + R[i])

    if ans >= INF:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    # 示例：n = 5
    main(5)