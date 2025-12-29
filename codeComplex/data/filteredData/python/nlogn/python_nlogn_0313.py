class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


def main(n):
    # 生成测试数据：1..n 的一个排列
    # 简单起见，使用升序排列
    a = list(range(1, n + 1))

    bi = Bit(n + 1)
    c = 0
    for i, x in enumerate(a):
        bi.add(x, 1)
        c += i + 1 - bi.sum(x)

    if c % 2 == n % 2:
        print("Petr")
    else:
        print("Um_nik")


if __name__ == "__main__":
    # 示例：可修改 n 测试
    main(5)