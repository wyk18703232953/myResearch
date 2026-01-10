def main(n):
    m = n // 2 + 1
    a = [(i * 2 + 1) % (n + 3) for i in range(n)]

    class BIT:
        def __init__(self, size):
            self.n = size
            self.data = [0] * (size + 1)

        def to_sum(self, i):
            s = 0
            while i > 0:
                s += self.data[i]
                i -= (i & -i)
            return s

        def add(self, i, x):
            while i <= self.n:
                self.data[i] += x
                i += (i & -i)

        def get(self, i, j):
            return self.to_sum(j) - self.to_sum(i - 1)

    def f(x, V):
        if x < V:
            return -1
        return 1

    def calc_median(M):
        b = [f(v, M) for v in a]
        res = 0
        c = [0]
        for x in b:
            c.append(c[-1] + x)
        d = [(c[i], i) for i in range(n + 1)]
        bit = BIT(2 * n + 10)
        offset = n + 1
        for value, index in d:
            if index == 0:
                bit.add(value + offset, 1)
                continue
            res += bit.get(1, value + offset - 1)
            bit.add(value + offset, 1)
        return res

    result = calc_median(m) - calc_median(m + 1)
    print(result)


if __name__ == "__main__":
    main(1000)