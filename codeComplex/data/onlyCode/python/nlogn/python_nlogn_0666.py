import sys
from array import array  # noqa: F401
import typing as Tp  # noqa: F401


def input():
    return sys.stdin.buffer.readline().decode('utf-8')


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


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [x for x in a if x != -1]
    mod = 998244353
    minus = n - len(b)
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

    print(ans % mod)


if __name__ == '__main__':
    main()
