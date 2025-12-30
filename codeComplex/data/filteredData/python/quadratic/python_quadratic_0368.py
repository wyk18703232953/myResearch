import random
import sys

mod = 10 ** 9 + 7
mod1 = 998244353


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


class Factorial:
    def __init__(self, MOD):
        self.MOD = MOD
        self.factorials = [1, 1]
        self.invModulos = [0, 1]
        self.invFactorial_ = [1, 1]

    def calc(self, n):
        if n <= -1:
            print("Invalid argument to calculate n!")
            print("n must be non-negative value. But the argument was " + str(n))
            sys.exit(0)
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
            print("Invalid argument to calculate n^(-1)")
            print("n must be non-negative value. But the argument was " + str(n))
            sys.exit(0)
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
            print("Invalid argument to calculate (n^(-1))!")
            print("n must be non-negative value. But the argument was " + str(n))
            sys.exit(0)
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
        return f.calc(n) * f.invFactorial(max(n - k, k)) * f.invFactorial(min(k, n - k)) % self.MOD


def powm(a, n, m):
    if a == 1 or n == 0:
        return 1
    if n % 2 == 0:
        s = powm(a, n // 2, m)
        return s * s % m
    else:
        return a * powm(a, n - 1, m) % m


def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = [x for _, x in sorted(zipped_pairs)]
    return z


def product(l):
    por = 1
    for i in range(len(l)):
        por *= l[i]
    return por


def binarySearchCount(arr, n, key):
    left = 0
    right = n - 1
    count = 0
    while left <= right:
        mid = int((right + left) / 2)
        if arr[mid] < key:
            count = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return count


def countdig(n):
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return c


def binary(x, length):
    y = bin(x)[2:]
    return y if len(y) >= length else "0" * (length - len(y)) + y


def countGreater(arr, n, k):
    l = 0
    r = n - 1
    leftGreater = n
    while l <= r:
        m = int(l + (r - l) / 2)
        if arr[m] >= k:
            leftGreater = m
            r = m - 1
        else:
            l = m + 1
    return n - leftGreater


def solve_from_grid(n, m, l):
    colsum = [[0 for _ in range(m)] for _ in range(n)]
    rowsum = [[0 for _ in range(m)] for _ in range(n)]
    col = [[0 for _ in range(m)] for _ in range(n)]
    row = [[0 for _ in range(m)] for _ in range(n)]
    tot = []

    for i in range(n):
        for j in range(m):
            if l[i][j] == '*':
                rowsum[i][j] = 1
                colsum[i][j] = 1
                row[i][j] = 1
                col[i][j] = 1

    for i in range(n):
        for j in range(1, m):
            if l[i][j] == '.':
                continue
            rowsum[i][j] += rowsum[i][j - 1]

    for i in range(n):
        for j in range(m - 2, -1, -1):
            if l[i][j] == '.':
                continue
            row[i][j] += row[i][j + 1]

    for i in range(m):
        for j in range(n - 2, -1, -1):
            if l[j][i] == '.':
                continue
            col[j][i] += col[j + 1][i]

    for i in range(m):
        for j in range(1, n):
            if l[j][i] == '.':
                continue
            colsum[j][i] += colsum[j - 1][i]

    def check(x, y):
        i = x
        j = y
        ans = min(row[i][j], rowsum[i][j], colsum[i][j], col[i][j]) - 1
        if ans == 0:
            return []
        return [ans]

    h = [[0 for _ in range(m + 1)] for _ in range(n)]
    v = [[0 for _ in range(m)] for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if l[i][j] == '*':
                ans_list = check(i, j)
                for j1 in ans_list:
                    tot.append([i + 1, j + 1, j1])
                    h[i][j - j1] += 1
                    h[i][j + j1 + 1] -= 1
                    v[i - j1][j] += 1
                    v[i + j1 + 1][j] -= 1

    for i in range(n):
        for j in range(1, m):
            h[i][j] += h[i][j - 1]

    for i in range(m):
        for j in range(1, n):
            v[j][i] += v[j - 1][i]

    for i in range(n):
        for j in range(m):
            if l[i][j] == '*' and h[i][j] == 0 and v[i][j] == 0:
                return -1, []

    return len(tot), tot


def generate_grid(n, m):
    # 随机生成一个由 '.' 和 '*' 组成的网格，保证至少有一个 '*'
    grid = []
    star_exists = False
    for _ in range(n):
        row = []
        for _ in range(m):
            if random.random() < 0.4:
                row.append('*')
                star_exists = True
            else:
                row.append('.')
        grid.append("".join(row))
    if not star_exists:
        # 强制在一个随机位置放一个 '*'
        i = random.randrange(n)
        j = random.randrange(m)
        row = list(grid[i])
        row[j] = '*'
        grid[i] = "".join(row)
    return grid


def main(n):
    # n 作为规模参数，构造一个大约为 n x n 的网格
    if n <= 0:
        n = 1
    rows = n
    cols = n
    l = generate_grid(rows, cols)
    cnt, tot = solve_from_grid(rows, cols, l)
    if cnt == -1:
        print(-1)
    else:
        print(cnt)
        for item in tot:
            print(*item)


if __name__ == "__main__":
    # 示例：默认用 n=5 运行
    main(5)