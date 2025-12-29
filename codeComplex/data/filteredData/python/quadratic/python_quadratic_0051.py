import random


class fenwick:
    """
    Fenwick Tree (Binary Indexed Tree) for prefix sums.
    1-indexed.
    """

    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)

    def to_sum(self, i):
        # return sum(a[1..i])
        s = 0
        while i > 0:
            s += self.data[i]
            i -= (i & -i)
        return s

    def add(self, i, x):
        # a[i] += x
        while i <= self.n:
            self.data[i] += x
            i += (i & -i)

    def get(self, i, j):
        # return sum(a[i..j])
        return self.to_sum(j) - self.to_sum(i - 1)


def main(n):
    # 1. 生成一个随机排列 permutation（1..n 的随机排列）
    permutation = list(range(1, n + 1))
    random.shuffle(permutation)

    # 2. 构造 seq，与原程序一致
    seq = [(permutation[i], i + 1) for i in range(n)]
    seq.sort(reverse=True)

    # 3. 生成测试查询：
    #    这里选择 m = n，随机生成 n 个区间 [l, r]
    m = n
    query = []
    for _ in range(m):
        l = random.randint(1, n)
        r = random.randint(l, n)
        query.append((l, r))

    # 4. 以下为原逻辑，无 input()，只使用上面生成的测试数据
    WHOLE_INVERSION = 0
    fenwick_1 = fenwick(n)

    for value, index in seq:
        WHOLE_INVERSION += fenwick_1.get(1, index)
        fenwick_1.add(index, 1)

    # 对每个查询输出 odd / even
    for l, r in query:
        d = r - l + 1
        WHOLE_INVERSION += d * (d - 1) // 2
        if WHOLE_INVERSION % 2 != 0:
            print("odd")
        else:
            print("even")


if __name__ == "__main__":
    # 示例：可自行修改 n 以生成不同规模的测试
    main(5)