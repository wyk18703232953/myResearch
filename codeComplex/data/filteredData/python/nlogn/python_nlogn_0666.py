import typing as Tp
import random


T = Tp.TypeVar('T')


class FenwickSum(Tp.Generic[T]):
    __slots__ = ['nodes', 'size', 'unit']

    def __init__(self, size: int, default: T, unit: T):
        self.nodes = [default] * (size + 1)
        self.size = size + 1
        self.unit = unit

    def add(self, index: int, value: T):
        while index < self.size:
            self.nodes[index] += value
            index += index & -index

    def sum(self, right: int) -> T:
        result = self.unit
        while right:
            result += self.nodes[right]
            right -= right & -right
        return result


def solve(a: Tp.List[int]) -> int:
    n = len(a)
    b = [x for x in a if x != -1]
    mod = 998244353
    minus = n - len(b)
    if minus == 0:
        # 原代码在 minus=0 时会 pow(0, mod-2, mod) 报错，这里直接处理
        # 只计算固定部分的逆序对
        bit = FenwickSum[int](n, 0, 0)
        ans = 0
        for x in reversed(b):
            ans += bit.sum(x)
            bit.add(x, 1)
        return ans % mod

    m_inv = pow(minus, mod - 2, mod)
    ans = 0

    bit = FenwickSum[int](n, 0, 0)
    for x in reversed(b):
        ans += bit.sum(x)
        bit.add(x, 1)

    ans += minus * (minus - 1) * pow(4, mod - 2, mod) % mod

    acc_u, m = [0] * (n + 1), minus
    for x in a:
        if x == -1:
            m -= 1
        else:
            acc_u[x] = m

    for i in range(n - 1, 0, -1):
        acc_u[i] += acc_u[i + 1]
        if acc_u[i] >= mod:
            acc_u[i] -= mod

    acc_d, m = [0] * (n + 1), minus
    for x in reversed(a):
        if x == -1:
            m -= 1
        else:
            acc_d[x] = m

    for i in range(1, n + 1):
        acc_d[i] += acc_d[i - 1]
        if acc_d[i] >= mod:
            acc_d[i] -= mod

    for x in set(range(1, n + 1)) - set(b):
        ans = (ans + (acc_u[x] + acc_d[x]) * m_inv) % mod

    return ans % mod


def generate_test_data(n: int) -> Tp.List[int]:
    """
    生成长度为 n 的测试数组 a：
    - 取值范围：-1 或 [1..n]
    - 随机放置若干个 -1，其余位置为 1..n 内随机值
    这只是用于测试的生成方式，不保证与原题的约束完全一致。
    """
    a = []
    for _ in range(n):
        if random.random() < 0.3:
            a.append(-1)
        else:
            a.append(random.randint(1, n))
    return a


def main(n: int):
    a = generate_test_data(n)
    ans = solve(a)
    print(ans)


if __name__ == '__main__':
    # 示例：调用 main(10)
    main(10)