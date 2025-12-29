import random

class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)

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
        # [i, j] (1 <= i <= j <= N)
        return self.to_sum(j) - self.to_sum(i - 1)


def f(x, V):
    if x < V:
        return -1
    return 1


def main(n):
    # 根据规模 n 生成测试数据
    # 这里生成 a 为 1..10^9 的随机整数，m 为 a 中元素的一个随机值
    global a
    random.seed(0)
    a = [random.randint(1, 10**9) for _ in range(n)]
    m = random.choice(a)

    def calc_median(M):
        b = [f(v, M) for v in a]
        res = 0
        c = [0]
        for x in b:
            c.append(c[-1] + x)
        d = [(c[i], i) for i in range(n + 1)]
        bit = BIT(2 * n + 10)
        for value, index in d:
            if index == 0:
                bit.add(value + n + 1, 1)
                continue
            res += bit.get(1, value + n)
            bit.add(value + n + 1, 1)
        return res

    print(calc_median(m) - calc_median(m + 1))


if __name__ == "__main__":
    # 示例：调用 main，规模自定
    main(10)