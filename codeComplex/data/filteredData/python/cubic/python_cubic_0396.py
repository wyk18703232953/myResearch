import random

# --------------------------- original helpers (kept as-is) ---------------------------

class SegmentTree:
    def __init__(self, data, default=0, func=lambda a, b: a + b):
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        if start == stop:
            return self.__getitem__(start)
        stop += 1
        start += self._size
        stop += self._size
        res = self._default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


class SegmentTree1:
    def __init__(self, data, default=10 ** 6, func=lambda a, b: min(a, b)):
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        if start == stop:
            return self.__getitem__(start)
        stop += 1
        start += self._size
        stop += self._size
        res = self._default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


MOD = 10 ** 9 + 7


class Factorial:
    def __init__(self, MOD):
        self.MOD = MOD
        self.factorials = [1, 1]
        self.invModulos = [0, 1]
        self.invFactorial_ = [1, 1]

    def calc(self, n):
        if n <= -1:
            raise ValueError("n must be non-negative")
        if n < len(self.factorials):
            return self.factorials[n]
        nextArr = [0] * (n + 1 - len(self.factorials))
        initialI = len(self.factorials)
        prev = self.factorials[-1]
        m = self.MOD
        for i in range(initialI, n + 1):
            prev = nextArr[i - initialI] = prev * i % m
        self.factorials += nextArr
        return self.factorials[n]

    def inv(self, n):
        if n <= -1:
            raise ValueError("n must be non-negative")
        p = self.MOD
        pi = n % p
        if pi < len(self.invModulos):
            return self.invModulos[pi]
        nextArr = [0] * (n + 1 - len(self.invModulos))
        initialI = len(self.invModulos)
        for i in range(initialI, min(p, n + 1)):
            nxt = -self.invModulos[p % i] * (p // i) % p
            self.invModulos.append(nxt)
        return self.invModulos[pi]

    def invFactorial(self, n):
        if n <= -1:
            raise ValueError("n must be non-negative")
        if n < len(self.invFactorial_):
            return self.invFactorial_[n]
        self.inv(n)
        nextArr = [0] * (n + 1 - len(self.invFactorial_))
        initialI = len(self.invFactorial_)
        prev = self.invFactorial_[-1]
        p = self.MOD
        for i in range(initialI, n + 1):
            prev = nextArr[i - initialI] = (prev * self.invModulos[i % p]) % p
        self.invFactorial_ += nextArr
        return self.invFactorial_[n]


class Combination:
    def __init__(self, MOD):
        self.MOD = MOD
        self.factorial = Factorial(MOD)

    def ncr(self, n, k):
        if k < 0 or n < k:
            return 0
        k = min(k, n - k)
        f = self.factorial
        return (
            f.calc(n)
            * f.invFactorial(max(n - k, k))
            * f.invFactorial(min(k, n - k))
            % self.MOD
        )


# --------------------------- core logic wrapped into main(n) ---------------------------

def main(n):
    """
    n: scale parameter; we derive grid size and k from it and generate test data.

    We will:
    - set rows = max(1, n)
    - set cols = max(1, min(n, 10))  # avoid huge memory
    - set k = 2 * min(n, 10)        # even k, not too large
    - generate random edge weights r (horizontal) and c (vertical)
    - run the original DP and print the resulting grid
    """

    # derive problem parameters from n (you can modify this policy if needed)
    rows = max(1, n)
    cols = max(1, min(n, 10))
    k = 2 * min(n, 10)  # must be even; DP is O(rows*cols*k)

    # random seed for reproducibility (optional)
    random.seed(1)

    # generate r: n x (m-1) non-negative weights
    r = [[random.randint(1, 9) for _ in range(cols - 1)] for _ in range(rows)]
    # generate c: (n-1) x m non-negative weights
    c = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows - 1)]

    if k % 2 == 1:
        # as in original code, output -1 grid for odd k
        a = [-1] * cols
        for _ in range(rows):
            print(*a)
        return

    half = k // 2
    INF = 10 ** 8
    # dp[i][j][x]: min cost to take exactly x steps and end at (i, j)
    dp = [[[0 for _ in range(half + 1)] for __ in range(cols)] for ___ in range(rows)]

    for x in range(1, half + 1):
        for i in range(rows):
            for j in range(cols):
                mn = INF
                if i > 0:
                    mn = min(mn, c[i - 1][j] + dp[i - 1][j][x - 1])
                if j > 0:
                    mn = min(mn, r[i][j - 1] + dp[i][j - 1][x - 1])
                if i < rows - 1:
                    mn = min(mn, c[i][j] + dp[i + 1][j][x - 1])
                if j < cols - 1:
                    mn = min(mn, r[i][j] + dp[i][j + 1][x - 1])
                dp[i][j][x] = mn

    for i in range(rows):
        row_out = []
        for j in range(cols):
            row_out.append(str(2 * dp[i][j][half]))
        print(" ".join(row_out))


if __name__ == "__main__":
    # example run with some scale n; adjust as desired
    main(5)