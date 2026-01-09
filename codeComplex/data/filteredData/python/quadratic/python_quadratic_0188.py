import sys

sys.setrecursionlimit(2 * 10**5 + 10)

write = lambda x: sys.stdout.write(x + "\n")
ninf = 0
op = max


class SG:
    def __init__(self, n, v=None):
        self._n = n
        self.geta = 0
        x = 0
        while (1 << x) < n:
            x += 1
        self._log = x
        self._size = 1 << self._log
        self._d = [ninf] * (2 * self._size)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def _update(self, k):
        self._d[k] = op(self._d[2 * k], self._d[2 * k + 1])

    def update(self, p, x):
        assert 0 <= p < self._n
        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            k = p >> i
            self._d[k] = op(self._d[2 * k], self._d[2 * k + 1])

    def get(self, p):
        assert 0 <= p < self._n
        return self._d[p + self._size]

    def check(self):
        return [self.get(p) for p in range(self._n)]

    def query(self, left, right):
        assert 0 <= left <= right <= self._n
        sml = ninf
        smr = ninf
        left += self._size
        right += self._size
        while left < right:
            if left & 1:
                sml = op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = op(self._d[right], smr)
            left >>= 1
            right >>= 1
        return op(sml, smr)

    def query_all(self):
        return self._d[1]

    def max_right(self, left, f):
        if left == self._n:
            return self._n
        left += self._size
        sm = ninf
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(op(sm, self._d[left])):
                        sm = op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = op(sm, self._d[left])
            left += 1
        return self._n

    def min_left(self, right, f):
        if right == 0:
            return 0
        right += self._size
        sm = ninf
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(op(self._d[right], sm)):
                        sm = op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = op(self._d[right], sm)
        return 0


def main(n):
    # n: input size -> length of array a
    # deterministic construction of a
    a = [(i * 37) ^ (i // 3) for i in range(n)]

    vs = [[0] * (n - i) for i in range(n)]
    vs[0] = a
    for i in range(1, n):
        for j in range(n - i):
            vs[i][j] = vs[i - 1][j] ^ vs[i - 1][j + 1]

    def f(l, r):
        return vs[r - l][l]

    ms = [[0] * n for _ in range(n)]
    for l in range(n):
        ms[l][l] = f(l, l)
        for r in range(l + 1, n):
            ms[l][r] = max(ms[l][r - 1], f(l, r))

    sgs = []
    for r in range(n):
        col = [ms[l][r] for l in range(r + 1)]
        sg = SG(len(col), col)
        sgs.append(sg)

    # number of queries scales with n
    q = n
    ans = []
    for i in range(q):
        # deterministic query generation, 1-based to match original, then converted
        l = (i * 2) % n
        r = n - 1 - (i % n)
        if l > r:
            l, r = r, l
        val = sgs[r].query(l, r + 1)
        ans.append(val)

    write("\n".join(map(str, ans)))


if __name__ == "__main__":
    main(1000)